from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from post.models import Post
from django.utils import timezone


def post_view(request,pid): 
    posts = get_object_or_404(Post,id=pid)
    context={'posts':posts}
    return render(request, "post.html", context)

