from django import forms
from .models import Profile,ProfileComment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['title','content']


class ProfileCommentForm(forms.ModelForm):
    class Meta:
        model = ProfileComment
        fields = ['content']