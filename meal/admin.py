from django.contrib import admin
from .models import Meals,Rating


class RatingAdmin(admin.ModelAdmin):
    list_display=['id','meal','user','stars']
    list_filter=['meal','user']
    
class MealAdmin(admin.ModelAdmin):
    list_display=['id','title','body']
    search_fields=['title','body']
    list_filter=['title','body']



admin.site.register(Meals)
admin.site.register(Rating)

# Register your models here.
