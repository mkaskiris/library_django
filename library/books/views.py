from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author

# Create your views here.

books = [
    {'id': 1,
        'title': 'Life, the Universe and Everything',
        'author': 'Douglas Adams'},
    {'id': 2,
        'title': 'The Meaning of Liff',
        'author': 'Douglas Adams'},
    {'id': 3,
        'title': 'The No. 1 Ladies\' Detective Agency',
        'author': 'Alexander McCall Smith'}
]


def index(req):
    print(list(Book.objects.all()))
    if list(Book.objects.all()) == []:
        # insert / initialise db
        jkrowling = Author(name='J.K. Rowling', country='U.K')
        jkrowling.save()
        jkrowling.book_set.create(title='Harry Potter')
    data = {'books': Book.objects.all()}
    # print(data['books'][0])
    return render(req, 'books/index.html', data)


def show(req, id):
    book = Book.objects.get(pk=id)
    return HttpResponse(f'<h3>You selected {book.title}</h3>')
