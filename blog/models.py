from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):  #this line defines that we are creating an object, class is a keyword
	author = models.ForeignKey('auth.User') # foreignkey = link to another model
	title = models.CharField(max_length=200) # charfield = text with limited number of characters
	text = models.TextField() # textfield = text without limit
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self): # def here means it is a function/method. Method always start with small letter. Model starts with
					   #uppercase
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title #method often returns something

	""" notice that publish and __str__ method were indented. This is because python is whitespace sensitive. If those 
		method weren't indented, python will not considered it belong to our Post class """


