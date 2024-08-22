from django.shortcuts import render
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.filter(status='published').order_by('-published_at')
    return render(request, 'index.html', {'blogs': blogs})
