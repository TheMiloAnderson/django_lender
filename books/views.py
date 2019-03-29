from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
import requests


@login_required
def book_detail_view(req, pk=None):
    book = get_object_or_404(
        Book,
        id=pk,
        user=req.user.id
    )
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q=+intitle:{ book.title }')
    data = response.json()
    context = {
        'book': book,
        'image_url': data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    }
    return render(req, 'book_detail.html', context)


@login_required
def book_list_view(req):
    context = {
        'books': get_list_or_404(Book, user=req.user.id)
    }
    return render(req, 'books_list.html', context)
