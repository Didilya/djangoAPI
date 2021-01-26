from django.db import models
from phone_field import PhoneField

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=80)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    comment = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.book