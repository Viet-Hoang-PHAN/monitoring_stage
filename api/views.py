# views.py consiste à définir une réponse du serveur en fonction de la demande

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from virtualmachine.models import Site, VirtualMachine, Gateway, Terminal, Service
from .renderers import JSONRenderer
from .serializers import SiteListSerializer, VMListSerializer, GatewayListSerializer,  TerminalListSerializer, ServiceListSerializer, UserListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from administration.models import Profile
from django.contrib.auth.models import User
from rest_framework import generics
from virtualmachine import upSaveDatabase


class SiteListApiView(ListAPIView):

	model = Site
	queryset = Site.objects.all()
	permissions_classes = (AllowAny, )
	renderer_classes = (JSONRenderer, )
	serializer_class = SiteListSerializer  

class SiteRetrieveApiView(APIView):

	def get(self, request, pk):
		site = Site.objects.get(pk=pk)
		serializer_class = SiteListSerializer(site).data
		return Response (serializer_class)


class VMListApiView(ListAPIView):
	model = VirtualMachine
	queryset = VirtualMachine.objects.all()
	permissions_classes = (AllowAny, )
	renderer_classes = (JSONRenderer, )
	serializer_class = VMListSerializer

class VMRetrieveApiView(APIView):

	def get(self, request, pk):
		vm = VirtualMachine.objects.get(pk=pk)
		serializer_class = VMListSerializer(vm).data
		return Response (serializer_class)

class GatewayListApiView(ListAPIView):
	model = Gateway
	queryset = Gateway.objects.all()
	permissions_classes = (AllowAny, )
	renderer_classes = (JSONRenderer, )
	serializer_class = GatewayListSerializer

class GatewayRetrieveApiView(APIView):

	def get(self, request, pk):
		gateway = Gateway.objects.get(pk=pk)
		serializer_class = GatewayListSerializer(gateway).data
		return Response (serializer_class)


class TerminalListApiView(ListAPIView):
	model = Terminal
	queryset = Terminal.objects.all()
	permissions_classes = (AllowAny, )
	renderer_classes = (JSONRenderer, )
	serializer_class = TerminalListSerializer

class TerminalRetrieveApiView(APIView):

	def get(self, request, pk):
		terminal = Terminal.objects.get(pk=pk)
		serializer_class = TerminalListSerializer(terminal).data
		return Response (serializer_class)

class ServiceListApiView(ListAPIView):
	model = Service
	queryset = Service.objects.all()
	permissions_classes = (AllowAny, )
	renderer_classes = (JSONRenderer, )
	serializer_class = ServiceListSerializer

class ServiceRetrieveApiView(APIView):

	def get(self, request, pk):
		service = Service.objects.get(pk=pk)
		serializer_class = ServiceListSerializer(service).data
		return Response (serializer_class)

	def put(self, request, pk):
		snippet = Service.objects.get(pk=pk)
		serializer_class = ServiceListSerializer(snippet, data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(ListAPIView):
	permissions_classes = (AllowAny, )
	queryset = User.objects.all()
	serializer_class = UserListSerializer
	renderer_classes = (JSONRenderer, )