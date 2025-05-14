from django.contrib import admin

from animal.models import Animal

# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_nome',)

admin.site.register(Animal, AnimalAdmin)