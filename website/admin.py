from django.contrib import admin
from . models import *
# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    list_display = ('header','title','message','image','status','date_created','last_updated')
    search_fields = ('header','title','message','image','status')
    list_filter = ('header','title','message','image','status','date_created','last_updated')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('header','title','rating','price','message','status','image','date_created','last_updated')
    search_fields = ('header','title','rating', 'price','message','status')
    list_filter = ('header','title','rating', 'price','message','status','date_created','last_updated')


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Content, ContentAdmin)
