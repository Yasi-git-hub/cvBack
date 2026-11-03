from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField()
    content=models.TextField()
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.TimeField(auto_now_add=True)
    updated_date=models.TimeField(auto_now=True)
    published_date=models.TimeField(null=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.id)
