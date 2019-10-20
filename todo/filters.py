from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    title = CharFilter(
        label='關鍵字', field_name='title', lookup_expr='icontains')
    category = ModelChoiceFilter(
        label='類別', field_name='category', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'category']
