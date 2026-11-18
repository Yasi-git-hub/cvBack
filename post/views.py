from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from post.models import Post
from django.utils import timezone


def post_view(request,pid): 
    # posts = get_object_or_404(Post,id=pid)
    # context={'posts':posts}
    # return render(request, "post.html", context)
    posts = list(Post.objects.all().order_by('id'))

    current_post = get_object_or_404(Post, id=pid)

    current_index = posts.index(current_post)

    previous_post = None
    next_post = None

    if current_index > 0:
        previous_post = posts[current_index - 1]

    if current_index < len(posts) - 1:
        next_post = posts[current_index + 1]

    context = {
        'posts': current_post,
        'previous_post': previous_post,
        'next_post': next_post,
    }

    return render(request, 'post.html', context)


def post_category(request, cat_name):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request, 'post/post_list.html', context)