from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile,ProfileComment
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ProfileCommentForm
from django.utils import timezone


def index(request):
    return render(request, 'pybo/pybo.html', {})


class ProfileViewList(ListView):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'
    ordering = ['-create_at']
    paginate_by = 10


@login_required(login_url='login')
def profile_create(request):
    if request.method =="POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.create_at = timezone.now()
            profile.save()
            return redirect('pybo:profile-list')
    else:
        form=ProfileForm()
    context = {'form':form}
    return render(request,'pybo/profile-create.html',context)

def profile_detail(request,profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    # comment = Comment.objects.filter(post=book).order_by(['-create_at'])
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ProfileCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.create_at = timezone.now()
                comment.profile = profile
                comment.save()
                return redirect('pybo:detail', profile_id)
        else:
            return redirect('login')
    else:
        form = ProfileCommentForm()
        liked = False
        if request.user in profile.like.all():
            liked = True
    context = {'profile':profile,'form':form,'liked':liked}
    return render(request, 'pybo/detail.html', context)


@login_required(login_url='login')
def delete_profile(request,profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.user.username == profile.author:
        profile.delete()
    return redirect('pybo:profile-list')

@login_required(login_url='login')
def update_profile(request,profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.method == 'POST':
        if request.user.username == profile.author:
            form = ProfileForm(request.POST,instance=profile)
            if form.is_valid:
                profile = form.save()
            return redirect('pybo:detail',profile_id)
    else:
        form=ProfileForm()
    context = {'profile': profile,'form': form}
    return render(request, 'pybo/profile-update.html', context)



@login_required(login_url='login')
def profile_like(request, profile_id):
    """
    책 추천하기 버튼 누르기
    """
    profile = get_object_or_404(Profile, pk=profile_id)
    profile.like.add(request.user)
    profile.save()
    return redirect('pybo:detail',profile_id)

@login_required(login_url='login')
def profile_unlike(request, profile_id):
    """
    책 추천 풀기
    """
    book = get_object_or_404(Profile, pk=profile_id)
    book.like.remove(request.user)
    book.save()
    return redirect('pybo:detail',profile_id)

def comment_delete(request, comment_id):
    """
    댓글 삭제
    """
    comment = get_object_or_404(ProfileComment, pk=comment_id)
    profile = comment.profile
    if request.user.username == comment.author:
        comment.delete()
    return redirect('pybo:detail',profile.id)

@login_required(login_url='login')
def comment_update(request, profile_id,comment_id):
    """
    댓글 수정하기
    """
    comment = get_object_or_404(ProfileComment, pk=comment_id)
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.method =="POST":
        form = ProfileCommentForm(request.POST,instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('pybo:detail',profile_id)
    else:
        form = ProfileCommentForm()
    liked = False
    if request.user in profile.like.all():
        liked = True
    context = {'profile': profile, 'form': form, 'liked': liked}
    return render(request, 'pybo/comment-update.html', context)


class UserProfileView(ListView):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user).order_by('-create_at')

