
from django.shortcuts import render


def post_view(request): 
    context={'title1':'how to become a back-end developer'}
    return render(request, "post.html", context)