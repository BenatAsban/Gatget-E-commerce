from django.contrib import admin
from .models import *

"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'discription')
    admin.site.register(Category,CategoryAdmin)

    """

admin.site.register(Category)
admin.site.register(Product)



