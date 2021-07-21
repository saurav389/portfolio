from django.contrib import admin
from .models import BlogPost, Category, BlogComment, CommentReply

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(BlogComment)
admin.site.register(CommentReply)