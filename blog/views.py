from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(req):
    blog = Blog.objects
    return render(req, 'blog/blog.html', {'blog': blog})


def article(req, article_id):
    article = get_object_or_404(Blog, pk=article_id)
    return render(req, 'blog/article.html', {'article': article})
