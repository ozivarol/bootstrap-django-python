from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=('id','name','created_date','genred','imdbrank','isPublished')
    list_display_links=('id','name')
    list_filter=('created_date','genred','imdbrank')
    list_editable=('isPublished',)
    search_fields=('name','genred')
    list_per_page=10

admin.site.register(Movie,MovieAdmin)