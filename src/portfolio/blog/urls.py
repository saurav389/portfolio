from django.urls import path
from .views import (BlogPostHome,
					PublicBlog,
					BlogPostNew,
					BlogPostView,
					BlogPostEdit,
					BlogPostDelete,
					Reply,
					blogcomment)


urlpatterns = [
    path('',PublicBlog,name='pubblog'),
    path('reply/',Reply,name='reply'),
    path('prblog',BlogPostHome,name='prblog'),
    path('new/',BlogPostNew,name='new'),
    path('<str:slug>/',BlogPostView,name="blogview"),
    path('comment',blogcomment,name='comment'),
    path('<str:slug>/edit',BlogPostEdit,name='edit'),
    path('<str:slug>/delete',BlogPostDelete)

]