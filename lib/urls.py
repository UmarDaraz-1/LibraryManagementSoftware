from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('book_detail/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book')
]
