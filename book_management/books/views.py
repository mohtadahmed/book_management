from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


@login_required
def dashboard(request):
    books = Book.objects.all()
    return render(request, 'books/dashboard.html', {'books': books})


