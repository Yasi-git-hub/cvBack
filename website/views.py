from django.shortcuts import render
from django.http import HttpResponse
def index_view(request):
    context={'title1':'how to become a backend developer'}
    return render(request,'index.html', context)
# Create your views here.
def about_view(request):
    return render(request,'about.html')

def contacts_view(request):
    return render(request,'contacts.html')