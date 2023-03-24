from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from .models import Book,Comment
from django.core.paginator import Paginator
from .forms import CommentForm
from django.utils import timezone
from django.contrib.auth.models import User


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

def book_detail(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    # comment = Comment.objects.filter(post=book).order_by(['-create_at'])
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_at = timezone.now()
            comment.post = book
            comment.save()
            return redirect('booker:detail',book_id)
    else:
        form = CommentForm()
        liked = False
        if request.user in book.like.all():
            liked = True
    context = {'book':book,'form':form,'liked':liked}
    return render(request, 'booker/book-detail.html', context)



def book_like(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.like.add(request.user)
    book.save()
    return redirect('booker:detail',book_id)



