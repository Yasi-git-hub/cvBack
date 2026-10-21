from django.urls import path
from website.views import *

app_name= 'website'

url_patterns={
    path('', index_view, name='index')
}