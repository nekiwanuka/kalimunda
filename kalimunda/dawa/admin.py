from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
#We give access to the admin to the sales
admin.site.register(Sale)
