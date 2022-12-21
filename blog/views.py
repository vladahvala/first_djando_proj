from django.shortcuts import render
from .models import Post

# Create your views here.
#дані збираються з бази даних, відправляються на html-сторінку, потім рендеряться(готуються) і відправляються назад користувачу

def blog_main(request, *args):
    posts = Post.objects.all()
    data_dict = {
        "posts": posts
    }
    return render(request, 'blog_main.html', data_dict)#запит, адреса, словник із даними

def slug_process(request, slug):
    post_slugs = [p.post_slug for p in Post.objects.all() ]
    if slug in post_slugs:
        post = Post.objects.get(post_slug = slug)
        data_dict = { 'post': post }
        return render(request, 'post_view.html', data_dict)
