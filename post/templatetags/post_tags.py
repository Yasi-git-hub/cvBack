from django import template
from post.models import Post, Category

register = template.Library()

@register.inclusion_tag('post/post_categories.html')
def postcategories():
    posts = Post.objects.all()
    categories = Category.objects.all()

    cat_dict = {}

    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()

    return {'categories': cat_dict}