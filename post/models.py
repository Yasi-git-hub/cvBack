from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    image=models.ImageField(upload_to='post/', default='post/default.jpg')
    author= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title=models.CharField()
    content=models.TextField()
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=True)
    created_date=models.TimeField(auto_now_add=True)
    updated_date=models.TimeField(auto_now=True)
    published_date=models.TimeField(null=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.id)
