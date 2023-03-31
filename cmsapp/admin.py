from django.contrib import admin
from cmsapp.models import Product

# Register your models here.
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=('title','details','cost')

admin.site.register(Product,ProductAdmin)