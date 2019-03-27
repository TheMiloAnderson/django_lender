from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book


def book_detail_view(req, pk=None):
    context = {
        'book': get_object_or_404(Book, id=pk)
    }
    return render(req, 'book_detail.html', context)


def book_list_view(req):
    context = {
        'books': get_list_or_404(Book)
    }
    return render(req, 'books_list.html', context)
