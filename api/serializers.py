#serializers.py pour choisir quelle information doit être montrée ou non

from rest_framework import serializers
from virtualmachine.models import Site, VirtualMachine, Gateway, Terminal, Service
from django.contrib.auth.models import User

class SiteListSerializer(serializers.ModelSerializer):

	class Meta: 
		model = Site 
		fields = ('id','name', 'adress', 'name_contact','tel_contact','email_contact','description')



class VMListSerializer(serializers.ModelSerializer):

	class Meta: 
		model = VirtualMachine 
		fields = ('id','site_id','name', 'ip', 'url')


class GatewayListSerializer(serializers.ModelSerializer):
	
	class Meta: 
		model = Gateway 
		fields = ('id', 'vm_id','gateway_id', 'conf_factory','conf1','conf2','conf3','conf4','conf5','mode','version','request_status','last_msg')

class TerminalListSerializer(serializers.ModelSerializer):
	
	class Meta: 
		model = Terminal 
		fields = ('id','gw_id','terminal_id', 'conf_factory','conf_rx','conf_tx','sample_rate','version','request_status','last_msg')


class ServiceListSerializer(serializers.ModelSerializer):
	
	class Meta: 
		model = Service 
		fields = ('id','gw_id','term_id','service_id','channel','label','enable','interruption','type_trigger','datatype','subsample_rate','high_threshold','low_threshold','delta','version')

	def update(self, instance, validated_data):

		instance.gw_id = validated_data.get('gw_id', instance.gw_id)
		instance.term_id = validated_data.get('term_id', instance.term_id)
		instance.service_id = validated_data.get('service_id', instance.service_id)
		instance.channel = validated_data.get('channel', instance.channel)
		instance.label = validated_data.get('label', instance.label)
		instance.enable = validated_data.get('enable', instance.enable)
		instance.interruption = validated_data.get('interruption', instance.interruption)
		instance.type_trigger = validated_data.get('type_trigger', instance.type_trigger)
		instance.datatype = validated_data.get('datatype', instance.datatype)
		instance.subsample_rate = validated_data.get('subsample_rate', instance.subsample_rate)
		instance.high_threshold = validated_data.get('high_threshold', instance.high_threshold)
		instance.low_threshold = validated_data.get('low_threshold', instance.low_threshold)
		instance.delta = validated_data.get('delta', instance.delta)
		instance.request_status = validated_data.get('request_status', instance.request_status)
		instance.version = validated_data.get('version', instance.version)
		
		instance.save()
		return instance

class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username','email']