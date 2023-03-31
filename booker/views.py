from django.shortcuts import render,get_object_or_404,redirect
from .models import Book,Comment
from django.core.paginator import Paginator
from .forms import CommentForm
from django.utils import timezone
import random
from django.db.models import Count
from django.contrib.auth.decorators import login_required

def index(request):
    """
    홈으로 가기
    """
    return render(request,'booker/home.html',{})

# class BookListView(ListView):
#     model = Book
#     template_name = 'booker/booklist.html'
#     context_object_name = 'booklist'
#     paginate_by = 10
#     ordering = ['-issued_at']
#     page_kwarg = 'page'

def book_list(request):
    page = request.GET.get('page','1')
    ca = request.GET.get('ca','recent')
    if ca == 'title':
        book_list = Book.objects.order_by('title')
    elif ca == 'liked':
        book_list = Book.objects.order_by('-issued_at')
        book_list = book_list.annotate(
            num_like=Count('like')).order_by('-num_like','-issued_at')
    elif ca == 'comment':
        book_list = Book.objects.order_by('-issued_at')
        book_list = book_list.annotate(
            num_comment=Count('comment')).order_by('-num_comment','-issued_at')
    else:
        book_list = Book.objects.order_by('-issued_at')

    paginator = Paginator(book_list,10)
    page_obj = paginator.get_page(page)
    context = {'booklist':page_obj,'page':page}
    return render(request,'booker/booklist.html',context)

def book_detail(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    # comment = Comment.objects.filter(post=book).order_by(['-create_at'])
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.create_at = timezone.now()
                comment.post = book
                comment.save()
                return redirect('booker:detail', book_id)
        else:
            return redirect('login')
    else:
        form = CommentForm()
        liked = False
        if request.user in book.like.all():
            liked = True
    context = {'book':book,'form':form,'liked':liked}
    return render(request, 'booker/book-detail.html', context)

@login_required(login_url='login')
def book_like(request, book_id):
    """
    책 추천하기 버튼 누르기
    """
    book = get_object_or_404(Book, pk=book_id)
    book.like.add(request.user)
    book.save()
    return redirect('booker:detail',book_id)


@login_required(login_url='login')
def book_unlike(request, book_id):
    """
    책 추천 풀기
    """
    book = get_object_or_404(Book, pk=book_id)
    book.like.remove(request.user)
    book.save()
    return redirect('booker:detail',book_id)




def book_reference(request):
    """
    랜덤 책 뽑기
    """
    book_id = random.randrange(1, 819)
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('booker:detail', book_id)
        else:
            return redirect('login')
    return render(request, 'booker/book-random.html')


def book_profile(request):
    """
    프로필 리스트 불러오기
    """
    sa = request.GET.get('sa','liked')
    page = request.GET.get('page','1')
    user = request.user
    if sa == 'comment':
        comments = Comment.objects.filter(author=request.user)
        book_list = [comment.post for comment in comments]
        book_title_set = set()
        books = []
        for book in book_list:
            if book.title not in book_title_set:
                book_title_set.add(book.title)
                books.append(book)
    else:
        books = Book.objects.filter(like=user)
    paginator = Paginator(books,7)
    page_obj = paginator.get_page(page)
    context = {'books': page_obj}
    return render(request, 'booker/profile.html', context)


@login_required(login_url='login')
def comment_delete(request, comment_id):
    """
    댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    if request.user == comment.author:
        comment.delete()
    return redirect('booker:detail',post.id)

@login_required(login_url='login')
def comment_update(request, book_id,comment_id):
    """
    댓글 수정하기
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    book = get_object_or_404(Book, pk=book_id)
    if request.method =="POST":
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('booker:detail',book_id)
    else:
        form = CommentForm()
    liked = False
    if request.user in book.like.all():
        liked = True
    context = {'book': book, 'form': form, 'liked': liked}
    return render(request, 'booker/book-update.html', context)


def about_us(request):
    return render(request ,'booker/aboutus.html', {})

