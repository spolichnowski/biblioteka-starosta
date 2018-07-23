from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from django.core.urlresolvers import reverse_lazy

from .models import Book, Author


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'author_list'
    paginate_by = 6


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    success_url = reverse_lazy('book_list')
    template_name = 'authors/author_create.html'
    fields = ['first_name', 'last_name', 'nationality']


class AuthorUpdateView(UpdateView):
    model = Author
    success_url = reverse_lazy('book_list')
    template_name = 'authors/author_create.html'
    fields = ['first_name', 'last_name', 'nationality']


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'author/list.html'
    context_object_name = 'book_list'
    paginate_by = 6


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(CreateView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'language', 'tags']


class BookUpdateView(UpdateView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'language', 'tags']


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('list')
