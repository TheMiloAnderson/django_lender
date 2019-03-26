from .views import book_detail_view, book_list_view
from django.urls import path

urlpatterns = [
    path('<int:pk>', book_detail_view, name='book_detail'),
    path('', book_list_view, name='book_list')
]
