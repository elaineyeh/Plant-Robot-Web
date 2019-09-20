from django.forms import ModelForm, Form, BooleanField

from .models import Post

class TodoModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['creator']

    def save(self, user, commit=True):
        todo = super().save(commit=False)
        todo.creator = user
        todo.save()

        self.save_m2m()

        return todo

class DeleteConfirmForm(Form):
    check = BooleanField(label='確定要刪除嗎？')