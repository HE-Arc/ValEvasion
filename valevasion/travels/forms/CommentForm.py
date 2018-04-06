from django import forms

from travels.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["article", "author", "pub_date", "isAccepted"]
