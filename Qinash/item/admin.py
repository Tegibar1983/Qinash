from django.contrib import admin

"""import database model"""
from .models import Category, Item

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)