from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.core.paginator import Paginator

def index(request):
    return render(request,'home.html',{})

# class BookListView(ListView):
#     model = Book
#     template_name = 'booker/booklist.html'
#     context_object_name = 'booklist'
#     paginate_by = 10
#     ordering = ['-issued_at']
#     page_kwarg = 'page'

def book_list(request):
    """
    list view
    """
    page = request.GET.get('page','1')

    book_list = Book.objects.order_by('-issued_at')

    paginator = Paginator(book_list,10)
    page_obj = paginator.get_page(page)
    context = {'booklist':page_obj,'page':page}
    return render(request,'booker/booklist.html',context)
