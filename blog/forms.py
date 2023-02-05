from django import forms
from .models import Post,  Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author',
                  'body', 'post_image')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Blog Title'
                }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Title Tag'
                }),
            # 'author': forms.Select(attrs={
            #     'class': 'form-control'
            #     }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '', 'id': 'post-author', 'type': 'hidden'
                }),



            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type Your Post'
                }),

        }


class ViewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author',
                  'body', 'post_image')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Blog Title'
                }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a Title Tag'
                }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'user_identifier',
                'type': 'hidden'
                }),

            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type Your Post'
                }),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
