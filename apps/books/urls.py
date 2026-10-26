from django.urls import path

from .views import BookListApi

urlpatterns = [
    path('books/', BookListApi.as_view()),
]
