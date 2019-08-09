from django.db import models
from django.contrib.auth.models import User
from virtualmachine.models import Site

class Profile(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	user_name = models.CharField(max_length=50)
	tel_contact = models.CharField(max_length=50)
	position = models.CharField(max_length=255)
	admin = models.BooleanField(default=False)
	developper = models.BooleanField(default=False)
	guest = models.BooleanField(default=True)

	def __str__(self):
		return '%s %s' %(self.site, self.position)
	