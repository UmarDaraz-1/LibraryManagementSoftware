from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    books = book.objects.all()
    #category = Categories.objects.all()
    #categories = ['Literature', 'Science', 'History', 'Law', 'Biography']
    return render(request, 'home.html', { 'books': books})

def book_detail(request):
    books = book.objects.all()
    return render(request, 'book_detail.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageUploadForm()
    return render(request, 'add_book.html', {'form': form})