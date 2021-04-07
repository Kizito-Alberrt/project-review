from django import forms

from .models import Post

class form(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add a title of your project'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add url '}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add author ', 'id': 'author'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }