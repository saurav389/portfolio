from django.urls import path
from .views import (BlogPostHome,
					PublicBlog,
					BlogPostNew,
					BlogPostView,
					BlogPostEdit,
					BlogPostDelete)


urlpatterns = [
    path('',PublicBlog,name='pubblog'),
    path('prblog',BlogPostHome,name='prblog'),
    path('new/',BlogPostNew,name='new'),
    path('<str:slug>/',BlogPostView),

    path('<str:slug>/edit',BlogPostEdit,name='edit'),
    path('<str:slug>/delete',BlogPostDelete)

]