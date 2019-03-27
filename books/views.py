from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book


@login_required
def book_detail_view(req, pk=None):
    context = {
        'book': get_object_or_404(
            Book,
            id=pk,
            user=request.user.id
        )
    }
    return render(req, 'book_detail.html', context)


@login_required
def book_list_view(req):
    context = {
        'books': get_list_or_404(Book, user=request.user.id)
    }
    return render(req, 'books_list.html', context)
