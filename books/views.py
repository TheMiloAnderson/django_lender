from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book
import requests
import json


@login_required
def book_detail_view(req, pk=None):
    book = get_object_or_404(
        Book,
        id=pk,
        user=req.user.id
    )
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q=+intitle:{book.title}')
    data = response.json()
    context = {
        'book': book,
        'image_url': data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    }
    return render(req, 'book_detail.html', context)


@login_required
def book_list_view(req):
    return render(req, 'books_list.1.html')


@login_required
def book_list_data(req):
    books = Book.objects.filter(user=req.user.id)
    books_list = []
    for book in books:
        books_list.append({
            'title': book.title,
            'author': book.author,
            'status': book.status,
            'id': book.id,
            'url': reverse('book_detail', args=(book.id,))
        })
    return HttpResponse(
        json.dumps(books_list),
        content_type='application/json'
    )
