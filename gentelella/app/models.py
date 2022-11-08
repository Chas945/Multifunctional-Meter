from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Meter(models.Model):

	meter_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=25)

	slave_id = models.IntegerField()

	ip_address = models.GenericIPAddressField()
	activate_status = models.BooleanField(default=False)


	class Meta:

		verbose_name = 'meter'
		verbose_name_plural = 'meters'


class Control(models.Model):

	control_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=25)
	desc = models.TextField(max_length = 250, null=True, blank=True)
	date = models.DateField(auto_now_add=True)
	status = models.BooleanField(default=False)

	class Meta:

		verbose_name = 'control'
		verbose_name_plural = 'controls'
	