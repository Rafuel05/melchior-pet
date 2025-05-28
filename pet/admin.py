from django.contrib import admin

from pet.models import Pet

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    prepopulated_fields={
        'slug':('pet_nome',)
    }
    list_display=('pet_nome','slug',)


admin.site.register(Pet,PetAdmin)

