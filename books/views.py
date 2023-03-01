from django.shortcuts import render
#generics
from django.views.generic import ListView
#my modells
from .models import Book


class BookListView(ListView):
    model = Book 
    templete_name = 'book_list.html'
