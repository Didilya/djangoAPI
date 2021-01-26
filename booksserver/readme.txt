# Booksserver django project

steps:
Set up Django\
Create a models: Book, Author, Order, User( I used buildin django.contrib.auth.models) in the database that the Django ORM will manage\
Set up the Django REST Framework\
Serialize the model from step 2\
Create the URI endpoints to view the serialized data\
Create User Registration and LoginIn with JWT
Setup Celery for email sending with delay

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pipx install pipenv
pip install django
pip install djangorestframework
pip install celery
pip install redis

```

## URL

```router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('order', OrderView.as_view()),   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

## Usage
```
python manage.py runserver
```

http://127.0.0.1:8000/order

http://127.0.0.1:8000/books/

http://127.0.0.1:8000/author/

http://127.0.0.1:8000/admin/

## Celery
to start server celery in in cmd under path \booksserver\booksserver
 run
```
celery -A booksserver worker -l INFO
 ```
[documentation](https://docs.celeryproject.org/en/stable/userguide/testing.html)