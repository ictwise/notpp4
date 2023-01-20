from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        posts = Post.objects.all()
        # friendly_names = [(c.id, c.get_friendly_name()) for c in comments]

        # self.fields['post'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'