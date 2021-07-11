from django.urls import path
from .views import (index_view,
					about_view,
					portfolio_view,
					contact_view)


urlpatterns = [
    path('',index_view,name='home'),
    path('about',about_view,name='about'),
    path('portfolio',portfolio_view,name='portfolio'),
    path('contact',contact_view,name='contact')

]