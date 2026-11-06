from django.urls import path
from website.views import *
from . import views

app_name= 'website'

urlpatterns={
    path('', views.index_view, name='index')
}