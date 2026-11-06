
from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post
from django.utils import timezone


def index_view(request):
    posts = Post.objects.filter(status=1)

    context = {
        'title1': 'how to become a backend developer',
        'posts': posts}

    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html')


def contacts_view(request):
    return render(request, 'contacts.html')

