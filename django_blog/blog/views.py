# from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# import post


"""posts = [
    {
        'author': 'Edward0rtiz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 4, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 5, 2020'
    }
]"""

# fun to handle traffic from home.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# fun to handle about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
