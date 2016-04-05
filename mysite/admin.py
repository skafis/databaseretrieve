from django.contrib import admin
from .models import View

# Register your models here.
# class ViewAdmin(admin.ModelAdmin):
#     list_display= ['message']
    
    
admin.site.register(View)