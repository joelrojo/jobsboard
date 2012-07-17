from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
import requests

# Create your views here.
def home(request, template='board/home.html'):
    c = {}
    return render_to_response(template, c, context_instance=RequestContext(request))

def search(request, template='board/search.html'):
    c = {}
    query = request.GET.get('query')
    query = query if query else ""
    location = request.GET.get('location')
    location = location if location else ""
    payload = {'publisher': '7575596370066104', 'v': '2', 'format': 'json', 'q': query, 'l': location}
    r = requests.get('http://api.indeed.com/ads/apisearch', params=payload)
    c['results'] = r.json
    return render_to_response(template, c, context_instance=RequestContext(request))
    