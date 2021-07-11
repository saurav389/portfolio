from django.contrib import admin
from .models import contact,homeDetail,experience,service,portfolio,about,contact,contactDetails
# Register your models here.
pages = [homeDetail,experience,service,portfolio,about,contact,contactDetails]
admin.site.register(pages)