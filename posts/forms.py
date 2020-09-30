from django import forms
from posts.models import Author

AUTHORS_CHOICES=()



class PostForm(forms.Form):
   author = forms.ModelChoiceField(queryset=Author.objects.all())
   title = forms.CharField()
   content = forms.CharField(widget=forms.Textarea)

   def clean(self):
       cleaned_data = super().clean()
       author = cleaned_data.get('author')
       title = cleaned_data.get('title')
       content = cleaned_data.get('content')

class AuthorForm(forms.Form):
   nick = forms.CharField()
   email = forms.EmailField()
   bio = forms.CharField(widget=forms.Textarea)

   def clean(self):
       cleaned_data = super().clean()
       author = cleaned_data.get('author')
       title = cleaned_data.get('title')
       content = cleaned_data.get('content')