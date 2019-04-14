from django.contrib import admin

# Register your models here.
from books.models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email']
    search_fields=('first_name','last_name',)
    list_filter=('first_name',)

class BookAdmin(admin.ModelAdmin):
    list_display=['title','publisher','publish_date']
    search_fields=('title','publisher',)
    list_filter=('publish_date',)
    date_hierarchy = 'publish_date'
    ordering = ('-title',)
    fields=('title','publisher','publish_date','authors',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
    
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)