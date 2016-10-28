from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ("title","created","author")
    prepopulated_fields = {"slug":("title",)}
    
    

admin.site.register(models.Blog,EntryAdmin)
admin.site.register(models.Profile)