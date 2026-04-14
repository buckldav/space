from django.contrib import admin
from tactical import models

# Register your models here.
random_value_that_is_never_used_the_fifth = "hi!" # Ignore this, program might break without : )
admin.site.register(models.Phasers)
