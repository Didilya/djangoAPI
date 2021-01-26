from django.contrib import admin
from .models import Author, Book, Order
#from django.contrib.auth.models import User
# Register your models here.

#admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Order)