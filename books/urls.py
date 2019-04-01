from .views import book_detail_view, book_list_view, book_list_data
from django.urls import path

urlpatterns = [
    path('<int:pk>', book_detail_view, name='book_detail'),
    path('', book_list_view, name='book_list'),
    path('data', book_list_data)
]
