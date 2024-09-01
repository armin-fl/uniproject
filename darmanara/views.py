from django.shortcuts import render , get_object_or_404
from . models import Blog
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='published')
    return render(request, 'blog_detail.html', {'blog': blog})


class archive_view(ListView):
    model = Blog
    template_name = 'archive.html'