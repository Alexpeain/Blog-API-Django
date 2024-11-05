from django_filters import rest_framework as filters
from .models import Post
from accounts.models import User  # Import the custom user model

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = filters.CharFilter(field_name='author', lookup_expr='exact')
    created_at = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Post
        fields = ['title', 'author', 'created_at']
