from django.db import models


class domain(models.Model):
	domain_text=models.CharField(max_length=255)
	freq=models.IntegerField(default=0)
	url1=models.CharField(max_length=255,default=0)

class word(models.Model):
	w=models.CharField(max_length=255)
	x=models.IntegerField(default=0)