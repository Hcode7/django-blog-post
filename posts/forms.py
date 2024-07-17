from django import forms
from .models import Comment

class PostForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    recipient_email = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email' , 'body')