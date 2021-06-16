from django.contrib import admin

from .models import *

class MovieImageInline(admin.TabularInline):
    model = Image
    max_num = 10
    min_num = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieImageInline, ]

admin.site.register(Category)



