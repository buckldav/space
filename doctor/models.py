from django.db import models

# Create your models here.

class IllCondition(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField()
	isCompleted=models.BooleanField(default=False)
	severity=models.IntegerField()
