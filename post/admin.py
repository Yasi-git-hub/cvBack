from django.contrib import admin
from post.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','status','created_date')
admin.site.register(Post,PostAdmin)