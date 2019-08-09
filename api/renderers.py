#renderers.py pour définir comment les données seront rendues
import json
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

class JSONRenderer(JSONRenderer):
	charset = 'utf-8'

	def render(self, data, media_type=None, renderer_context=None):
		super(JSONRenderer, self).render(data)

		return json.dumps({'data': data})