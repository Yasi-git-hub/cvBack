from django.urls import path, include
from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    # path("", views.post_view, name="detail"),
    path('<int:pid>/', views.post_view, name='detail' ),
    path('category/<str:cat_name>', views.post_category, name='category')
]