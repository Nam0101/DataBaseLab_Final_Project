from django.shortcuts import render

# Create your views here.


def bookPage(request):
    return render(request, 'book/book.html')
