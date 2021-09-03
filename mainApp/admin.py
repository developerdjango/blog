from django.contrib import admin
from mainApp.models import Teams
from django.utils.html import format_html


# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.photo.url))

    thumbnail.short_description= 'photo'
    list_display = ['id', 'thumbnail','first_name', 'last_name', 'designation','created_date']
    search_fields = ('id','first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Teams, TeamsAdmin)
