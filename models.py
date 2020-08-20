from django.db import models

class Lotto(models.Model):
	number1 = models.TextField(blank=True,null=True)
	number2 = models.TextField(blank=True,null=True)
	number3 = models.TextField(blank=True,null=True)
	number4 = models.TextField(blank=True,null=True)
	number5 = models.TextField(blank=True,null=True)
	number6 = models.TextField(blank=True,null=True)

	def __str__(self):
		return "{} - {}".format(self.number1,self.number2)

# Create your models here.
