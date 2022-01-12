from django.contrib import admin
from .models import Cars

from django.utils.html import format_html
# Register your models here.


class CarsAdmin(admin.ModelAdmin):
    
    def thumbnail(self, obj):
        return format_html("<img src='{}' width=50 style='border-radius: 40%;'  />".format(obj.car_photo.url))
    
    def colorcard(self, obj):
        return format_html("<div class=\"colorcard\" style=\"border-radius: 20%;background-color: {};height: 20px; width: 75% ;border: 5px wheat solid;\"></div>".format(obj.color.lower()))
    
    thumbnail.short_description = 'Car Image'
    colorcard.short_description = 'Color'    
    
    list_display = ('id', 'thumbnail', 'car_title','city', 'colorcard', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title',)
    search_fields = ('city', 'color', 'model', 'id', 'body_style', 'fuel_type',)
    list_filter = ('city', 'color', 'model', 'car_title', 'body_style', 'fuel_type',)
    list_editable = ( 'is_featured',)
    

admin.site.register(Cars, CarsAdmin)