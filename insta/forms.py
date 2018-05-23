from django import forms
from .models import Profile,Image,Comment

class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','profile']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','following']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
       


