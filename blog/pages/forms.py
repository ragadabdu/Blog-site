from django import forms
from .models import Post

INPUT_CLASSES = 'w-full h-10 rounded-lg px-4 mb-5'

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','keyword')

        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'content' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }),
            'keyword' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
        }

class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','keyword')

        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'content' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }),
            'keyword' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
        }