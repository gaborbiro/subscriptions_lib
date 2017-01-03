from django.contrib import admin
from .models import Subcategory, Category, Company, Subscription

# Register your models here.
myModels = [Category, Subcategory, Company, Subscription]

admin.site.register(myModels)
