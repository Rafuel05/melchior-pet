from django.contrib import admin

from animal.models import Animal

# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('animal_nome',)
    }
    list_display = ('animal_nome','slug',)

admin.site.register(Animal, AnimalAdmin)