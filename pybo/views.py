from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
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
    if request.method ==" POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.create_at = timezone.now()
            profile.save()
    else:
        form=ProfileForm()
    context = {'form':form}
    return render(request,'pybo/profile-create.html',context)

