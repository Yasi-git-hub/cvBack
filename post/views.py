
from django.shortcuts import render
from post.models import Post
from django.utils import timezone


def post_view(request): 
    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.localtime().time()
    )
    context={'posts':posts}
    return render(request, "post.html", context)

