from django.contrib import admin
from tactical import models

# Register your models here.
random_value_that_is_never_used_the_fifth = "hi!" # Ignore this, program might break without : )

class PhasersAdmin(admin.ModelAdmin):
    list_display = ['phaser_is_working', 'direction_fireing']
    list_filter = ['phaser_is_working', 'direction_fireing']


admin.site.register(models.Phasers, PhasersAdmin)