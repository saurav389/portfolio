from django.db import models
from PIL import Image

# Create your models here.
class homeDetail(models.Model):
	home_title = models.CharField(max_length=120)
	title_blue = models.CharField(max_length=120)
	paragraph = models.TextField(max_length=500)

	def __str__(self):
		return self.home_title

class experience(models.Model):
	skill = models.CharField(max_length=120)
	percent = models.IntegerField()

	def __str__(self):
		return self.skill

class service(models.Model):
	skill = models.CharField(max_length=120)
	skillPink = models.CharField(max_length=120)
	image = models.ImageField(upload_to='skill/%Y/%m/%d', blank=True, null=True)
	paragraph = models.TextField(max_length=500)



	def __str__(self):
		return f"{self.skill} {self.skillPink}"

	# def save(self):
	#     super().save()
	#     img = Image.open(self.image.path)
	#     if img.height>300 or img.width>300:
	#         output_size = (700,300)
	#         img.thumbnail(output_size)
	#         img.save(self.image.path)

class portfolio(models.Model):
	image = models.ImageField(upload_to='skill/%Y/%m/%d', blank=True, null=True)
	detail = models.CharField(max_length=120)

	def __str__(self):
		return self.detail

class about(models.Model):
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to='skill/%Y/%m/%d', blank=True, null=True)
	paragraph = models.TextField(max_length=500)


	def __str__(self):
		return self.title

class contact(models.Model):
	name = models.CharField(max_length=120)
	company   = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	subject = models.CharField(max_length=120)
	message = models.TextField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
	    ordering = ['-updated', '-timestamp']


	def __str__(self):
		return f"{self.name} From {self.company} company --------------  Date: {self.timestamp} "

class contactDetails(models.Model):
	title = models.CharField(max_length=120)
	titleBlue = models.CharField(max_length=120)
	paragraph = models.TextField(max_length=500)
	email = models.EmailField(max_length=120)
	mobileNo = models.IntegerField()
	address = models.CharField(max_length=120)

	def __str__(self):
		return self.title