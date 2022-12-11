from django.shortcuts import render

# Create your views here.

def blog_main(request, *args):
    return render(request, 'blog_main.html', {})
