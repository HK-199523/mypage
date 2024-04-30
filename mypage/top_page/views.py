from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsPost

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'news'
    model = NewsPost
    def get_queryset(self):
        return NewsPost.objects.order_by('-posted_at')[:4]