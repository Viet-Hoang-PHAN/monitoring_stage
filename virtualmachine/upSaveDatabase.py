from virtualmachine.models import Gateway, Terminal, VirtualMachine, Service

import requests
import json


class tcheckGateway():
	url ='https://datacenter2.misnet.fr/datacenter/gateways'
	data = requests.get(url=url)
	dataset = json.loads(data.content.decode('utf-8'))
	
	compteur = 0

	for gateways in dataset :
		conf1 = dataset[compteur]["conf1"]
		conf2 = dataset[compteur]["conf2"]
		conf3 = dataset[compteur]["conf3"]
		conf4 = dataset[compteur]["conf4"]
		conf5 = dataset[compteur]["conf5"]
		conf_factory = dataset[compteur]["conf_factory"]
		vm_id = 1
		gateway_id = dataset[compteur]["id"]
		last_msg = dataset[compteur]["last_msg"]
		mode = dataset[compteur]["mode"]
		request_status = dataset[compteur]["request_status"]
		version = dataset[compteur]["version"]

		if Gateway.objects.filter(gateway_id = gateway_id):

			gateway = Gateway.objects.get(gateway_id = gateway_id)
			gateway.conf_factory = conf_factory
			gateway.conf1 = conf1
			gateway.conf2 = conf2
			gateway.conf3 = conf3
			gateway.conf4 = conf4
			gateway.conf5 = conf5
			gateway.mode = mode
			gateway.version = version
			gateway.request_status = request_status
			gateway.last_msg = last_msg
			gateway.save()

		else: 

			gateway = Gateway()
			gateway.vm_id = VirtualMachine.objects.get(id=1)
			gateway.gateway_id = int(gateway_id)
			gateway.conf_factory = conf_factory
			gateway.conf1 = conf1
			gateway.conf2 = conf2
			gateway.conf3 = conf3
			gateway.conf4 = conf4
			gateway.conf5 = conf5
			gateway.mode = mode
			gateway.version = version
			gateway.request_status = request_status
			gateway.last_msg = last_msg
			gateway.save()


		compteur=compteur+1


class tcheckTerminal():

	url ='https://datacenter2.misnet.fr/datacenter/terminals'
	data = requests.get(url=url)
	dataset = json.loads(data.content.decode('utf-8'))
	
	compteur = 0


	for terminals in dataset :

		gw_id = dataset[compteur]["gw_id"]
		terminal_id = dataset[compteur]["id"]
		conf_factory = dataset[compteur]["conf_factory"]
		conf_rx = dataset[compteur]["conf_rx"]
		conf_tx = dataset[compteur]["conf_tx"]
		sample_rate = dataset[compteur]["sample_rate"]
		version = dataset[compteur]["version"]
		request_status = dataset[compteur]["request_status"]
		last_msg = dataset[compteur]["last_msg"]
		

		if Terminal.objects.filter(terminal_id = terminal_id) :

			terminal = Terminal.objects.get(terminal_id = terminal_id)

			terminal.gw_id = Gateway.objects.get(gateway_id=gw_id)
			terminal.conf_factory = conf_factory
			terminal.conf_rx = conf_rx
			terminal.conf_tx = conf_tx
			terminal.sample_rate = sample_rate
			terminal.version = version
			terminal.request_status = request_status
			terminal.last_msg = last_msg
			terminal.save()
		else: 

			terminal = Terminal()
			terminal.gw_id = Gateway.objects.get(gateway_id=gw_id)
			terminal.terminal_id = int(terminal_id)
			terminal.conf_factory = conf_factory
			terminal.conf_rx = conf_rx
			terminal.conf_tx = conf_tx
			terminal.sample_rate = int(sample_rate)
			terminal.version = version
			terminal.request_status = request_status
			terminal.last_msg = last_msg
			terminal.save()
			

		compteur=compteur+1

class tcheckService():

	url ='https://datacenter2.misnet.fr/datacenter/services'
	data = requests.get(url=url)
	dataset = json.loads(data.content.decode('utf-8'))
	
	compteur = 0

	for services in dataset :

		gw_id =dataset[compteur]["gw_id"]	
		term_id = dataset[compteur]["term_id"]	
		service_id = dataset[compteur]["id"]
		channel = dataset[compteur]["channel"]
		label = dataset[compteur]["label"]
		enable = dataset[compteur]["enable"]
		interruption = dataset[compteur]["interruption"]
		type_trigger = dataset[compteur]["trigger_mode"]
		datatype = dataset[compteur]["datatype"]
		subsample_rate = dataset[compteur]["subsample_rate"]
		high_threshold = dataset[compteur]["high_threshold"]
		low_threshold = dataset[compteur]["low_threshold"]
		delta = dataset[compteur]["delta"]
		request_status = dataset[compteur]["request_status"]
		version = dataset[compteur]["version"]
		key = compteur+ 1

		if Service.objects.filter(key = key) :
			service = Service.objects.get(key = key)
			service.gw_id = Gateway.objects.get(gateway_id=gw_id)
			service.term_id = Terminal.objects.get(terminal_id=term_id)
			service.channel = int(channel)
			service.label = label
			service.enable = enable
			service.interruption = interruption
			service.type_trigger = type_trigger
			service.datatype = datatype
			service.subsample_rate = int(subsample_rate)
			service.high_threshold = high_threshold
			service.low_threshold = low_threshold
			service.delta = delta
			service.request_status = request_status
			service.version = version

		else:
			service = Service()

			service.gw_id = Gateway.objects.get(gateway_id=gw_id)
			service.term_id = Terminal.objects.get(terminal_id=term_id)
			service.service_id = int(service_id)
			service.channel = int(channel)
			service.label = label
			service.enable = enable
			service.interruption = interruption
			service.type_trigger = type_trigger
			service.datatype = datatype
			service.subsample_rate = int(subsample_rate)
			service.high_threshold = high_threshold
			service.low_threshold = low_threshold
			service.delta = delta
			service.request_status = request_status
			service.version = version
			service.key = key

			service.save()

		compteur=compteur+1