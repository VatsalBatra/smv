from django.db import models

# Create your models here.
class image_slide(models.Model):
	slide_image = models.ImageField(blank = False);
	caption = models.CharField(max_length = 1024,default = " " ,blank = True);
class achievement(models.Model):
	achievments_image = models.ImageField(blank = False);
	title = models.CharField(max_length = 1024,default = " ",blank = True);
	content = models.TextField(max_length = 1024,default = " ",blank = True);
	date = models.CharField(max_length = 1024,default = " ",blank = True);

class our_ride(models.Model):
	our_ride_image = models.ImageField(blank = False);
	title = models.CharField(max_length = 1024,default = " ",blank = True);

class crew_sir(models.Model):
	sir_img = models.ImageField(blank = False);
	title = models.CharField(max_length = 1024,default = " " ,blank = True);
	text_1 = models.CharField(max_length = 1024,default = " " ,blank = True);
	text_2 = models.CharField(max_length = 1024,default = " " ,blank = True);
	text_3 = models.CharField(max_length = 1024,default = " " ,blank = True);

class crew_members(models.Model):
	title = models.CharField(max_length = 1024,default = " " ,blank = True);
class partners(models.Model):
	logo = models.ImageField(blank = False);
	name = models.CharField(max_length = 1024,default = " " ,blank = True);
	links = models.CharField(max_length = 1024,default = " " ,blank = True);
