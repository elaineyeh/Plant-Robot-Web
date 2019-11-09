from django.forms import ModelForm, Form, BooleanField

from .models import Post

class TodoModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['user_id']

    def save(self, user, commit=True):
        todo = super().save(commit=False)
        todo.user_id = user
        todo.save()

        self.save_m2m()

        return todo

class DeleteConfirmForm(Form):
    check = BooleanField(label='確定要刪除嗎？')