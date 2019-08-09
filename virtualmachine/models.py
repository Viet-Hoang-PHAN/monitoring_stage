from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Site(models.Model):
	name = models.CharField(max_length=200)
	adress = models.CharField(max_length=200)
	name_contact = models.CharField(max_length=200)
	tel_contact = models.CharField(max_length=200)
	email_contact = models.CharField(max_length=200)
	description = models.TextField()


class VirtualMachine(models.Model):
	site_id = models.ForeignKey(Site, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	ip = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	user = models.CharField(max_length=200)
	pwd = models.CharField(max_length=200)

	def __str__(self):
		return '%s %s %s %s %s %s ' %(self.site_id, self.name, self.ip, self.url, self.user, self.pwd)



class Gateway(models.Model):
	vm_id = models.ForeignKey(VirtualMachine, on_delete=models.CASCADE)
	gateway_id =  models.IntegerField(default=None)
	conf_factory = models.CharField(max_length=200)
	conf1 = models.CharField(max_length=200)
	conf2 = models.CharField(max_length=200)
	conf3 = models.CharField(max_length=200)
	conf4 = models.CharField(max_length=200)
	conf5 = models.CharField(max_length=200)
	mode = models.CharField(max_length=200)
	version = models.CharField(max_length=200)
	request_status = models.CharField(max_length=200)
	last_msg = models.FloatField(default=None)

	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s %s %s %s' %(self.vm_id, self.gateway_id, self.conf_factory, self.conf1, self.conf2, self.conf3, self.conf4, self.conf5, self.mode, self.version, self.request_status, self.last_msg)

class Terminal(models.Model):
	gw_id = models.ForeignKey(Gateway, on_delete=models.CASCADE)
	terminal_id =  models.IntegerField(default=None)
	conf_factory = models.CharField(max_length=200)
	conf_rx = models.CharField(max_length=200)
	conf_tx = models.CharField(max_length=200)
	sample_rate = models.IntegerField(default=None)
	version = models.CharField(max_length=200)
	request_status = models.CharField(max_length=200)
	last_msg = models.FloatField(default=None)

	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s' %( self.gw_id, self.terminal_id, self.conf_factory, self.conf_rx, self.conf_tx, self.sample_rate, self.version, self.request_status, self.last_msg)

class Service(models.Model):
	gw_id = models.ForeignKey(Gateway,on_delete=models.CASCADE)
	term_id = models.ForeignKey(Terminal,on_delete=models.CASCADE)
	service_id =  models.IntegerField(default=None)
	channel = models.IntegerField(default=None)
	label = models.CharField(max_length=200)
	enable = models.BooleanField(default=True)
	interruption = models.BooleanField(default=True)
	type_trigger = models.IntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(2)])
	datatype = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(31)])
	subsample_rate = models.IntegerField(default=None, blank =True, null=True)
	high_threshold = models.FloatField(default=None, blank =True, null=True)
	low_threshold = models.FloatField(default=None,blank =True, null=True)
	delta = models.FloatField(default=None, blank =True, null=True)
	request_status = models.CharField(max_length=200,default=None, blank =True, null=True)
	version = models.CharField(max_length=200,default=None, blank =True, null=True)
	key = models.IntegerField(default=None)
	def __str__(self):
		return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %( self.gw_id, self.term_id, self.service_id ,self.channel, self.label, self.enable, self.interruption, self.type_trigger, self.datatype, self.subsample_rate, self.high_threshold, self.low_threshold, self.delta, self.request_status, self.version, self.key)