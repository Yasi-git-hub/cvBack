
from django.shortcuts import render,redirect
from django.http import HttpResponse
from post.models import Post
from django.utils import timezone
from website.models import contact
from website.forms import ContactForm
from django.contrib import messages


def index_view(request):
    posts = Post.objects.filter(status=1)

    context = {
        'title1': 'how to become a backend developer',
        'posts': posts}

    return render(request, 'index.html', context)


def about_view(request):
    return render(request, 'about.html')


def contacts_view(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
        return redirect('/')

    return redirect('/')

# render(request,'index.html',{'form':form})