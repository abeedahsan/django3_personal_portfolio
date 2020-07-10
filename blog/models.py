from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)


	date = models.DateField(max_length=100)
	description = models.TextField(max_length=10000000000000000000000000000)



	def __str__(self):
		return self.title

