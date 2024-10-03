from django.contrib import admin
from .models import Kitten, Breed

class KittensAdmin(admin.ModelAdmin):
    list_display = 'pk', 'breed', 'color', 'age', 'description', 'grade'

class BreedAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'

admin.site.register(Kitten, KittensAdmin)
admin.site.register(Breed, BreedAdmin)
