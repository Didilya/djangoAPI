from django.urls import include, path
from rest_framework import routers
from . import views
from .views import BookViewSet, AuthorViewSet, RegisterView,LoginView, OrderView

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('order', OrderView.as_view()),   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]