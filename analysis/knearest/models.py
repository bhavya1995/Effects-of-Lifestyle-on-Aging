from django.db import models

# Create your models here.

class accuracyallcol(models.Model):
	x = models.CharField(max_length = 255, null = True)
	prediction = models.IntegerField(null = True)
	original = models.IntegerField(null = True)
	counttrue = models.IntegerField(null = True)
	counttotal = models.IntegerField(null = True)

class accuracyexceptbig(models.Model):
	x = models.CharField(max_length = 255, null = True)
	prediction = models.IntegerField(null = True)
	original = models.IntegerField(null = True)
	counttrue = models.IntegerField(null = True)
	counttotal = models.IntegerField(null = True)

class accuracyonlybig(models.Model):
	x = models.CharField(max_length = 255, null = True)
	prediction = models.IntegerField(null = True)
	original = models.IntegerField(null = True)
	counttrue = models.IntegerField(null = True)
	counttotal = models.IntegerField(null = True)

class predictallcol (models.Model):
	x = models.CharField(max_length = 255, null = True)
	prediction = models.IntegerField(null = True)

class predictexceptbig (models.Model):
	x = models.CharField(max_length = 255, null = True)
	prediction = models.IntegerField(null = True)

class predictonlybig (models.Model):
	x = models.CharField(max_length = 255, null = True)
	prediction = models.IntegerField(null = True)
