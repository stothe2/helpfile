from django.db import models

# Create your models here.
class APMControls(models.Model):
	item_name = models.CharField(max_length=200)
	feature = models.TextField(max_length=200)
	settings = models.TextField()
	comments = models.TextField(blank=True)
	#extra = models.TextField(blank=True)

class PMControls(models.Model):
	item_name = models.CharField(max_length=200)
	feature = models.TextField(max_length=200)
	settings = models.TextField()
	comments = models.TextField(blank=True)

class TMControls(models.Model):
	item_name = models.CharField(max_length=200)
	feature = models.TextField(max_length=200)
	settings = models.TextField()
	comments = models.TextField(blank=True)

class UIControls(models.Model):
	item_name = models.CharField(max_length=200)
	feature = models.TextField(max_length=200)
	settings = models.TextField()
	comments = models.TextField(blank=True)

	def __unicode__(self):
		return self.item_name
