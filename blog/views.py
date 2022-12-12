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
