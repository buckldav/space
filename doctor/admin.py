from django.contrib import admin
from .models import IllCondition
# Register your models here.

@admin.register(IllCondition)
class IllConditionAdmin(admin.ModelAdmin):
	pass



