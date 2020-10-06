from django import forms
from posts.models import Author

AUTHORS_CHOICES=()



class PostForm(forms.Form):
   author = forms.ModelChoiceField(queryset=Author.objects.all())
   title = forms.CharField()
   content = forms.CharField(widget=forms.Textarea)


class AuthorForm(forms.Form):
   nick = forms.CharField()
   email = forms.EmailField()
   bio = forms.CharField(required=False,widget=forms.Textarea)
