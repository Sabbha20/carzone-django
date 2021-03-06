from django.contrib import admin
from .models import Team

from django.utils.html import format_html


# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return obj.first_name+" "+obj.last_name
    
    def thumbnail(self, obj):
        return format_html("<img src='{}' width=40 style='border-radius: 40%;'  />".format(obj.photo.url))
    
    thumbnail.short_description = 'Image'
    
    list_display = ('id','thumbnail', 'full_name', 'designation', 'created_date')
    list_display_links = ('id', 'full_name', 'thumbnail',)
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)