
from django.shortcuts import render


def post_view(request):
    return render(request, "post.html")