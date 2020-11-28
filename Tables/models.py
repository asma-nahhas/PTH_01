from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Table(models.Model):
	name=models.CharField(max_length=200)
	fileName=models.CharField(max_length=200,null=True)
	fileIndex=models.IntegerField(null=True)
	created_at=models.DateTimeField(default=datetime.now,blank=True)
	def __str__(self):
		return self.name
	
