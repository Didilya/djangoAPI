from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer, UserSerializer,OrderSerializer
from .models import Book, Author
from django.http import HttpResponse
from django.conf import settings
from django.contrib import auth
import jwt
from .tasks import sleepy, send_email_task

def index(request):
    # Sending mail with Celery
    send_email_task.delay()
    return HttpResponse('<h1>Email has been send</h1>')



class RegisterView(generics.GenericAPIView):
    # New user registration
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    # User login
    serializer_class = UserSerializer
    def post(self,request):
        data=request.data
        username=data.get('username','')
        password=data.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user:
            auth_token = jwt.encode({'username':user.username},settings.JWT_SECRET_KEY)
            serializer=UserSerializer(user)
            data={'user': serializer.data, 'token': auth_token
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        



class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

class OrderView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        data=request.data
        if serializer.is_valid():
            serializer.save()
            index(request)
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



