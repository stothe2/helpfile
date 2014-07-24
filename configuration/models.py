from django.db import models

# Create your models here.
class Controls(models.Model):
	item_name = models.CharField(max_length=200)
	feature = models.TextField(max_length=200)
	settings = models.TextField()
	comments = models.TextField(blank=True)
	additional_comments = models.TextField(blank=True)

	def __unicode__(self):
		return self.item_name

	def get_model_name(self):
		return self.__class__.__name__

	class Meta:
		abstract=True

class APM(Controls):
	pass

class PM(Controls):
	pass

class TM(Controls):
	pass

class UI(Controls):
	pass
