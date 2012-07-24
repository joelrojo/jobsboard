from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
import requests
import json

# Create your views here.
def home(request, template='board/home.html'):
    c = {}
    return render_to_response(template, c, context_instance=RequestContext(request))

def search(request):
    c = {}
    query = request.GET.get('query', '')
    location = request.GET.get('location', '')
    results_counter= request.GET.get('results_counter', '')
    payload = {'publisher': '7575596370066104', 'v': '2', 'format': 'json', 'q': query, 'l': location, 'start' : results_counter}
    r = requests.get('http://api.indeed.com/ads/apisearch', params=payload)
    json_decoded = json.loads(r.text)
    
    # check if there are results
    if json_decoded['totalResults'] == 0:
        c['results'] = 'No search results. Please Try again.'
    else:
        c['results'] = ''
    
    # iterate through results and parse html
    results = json_decoded['results']
    for r in results:
        c['results'] += '<div class="job-block">'
        c['results'] += '<h3>' + r['jobtitle'] + '</h3>'
        c['results'] += '<h4>' + r['source'] + '</h4>'
        c['results'] += '<h5>Location: ' + r['formattedLocation'] + '</h5>'
        c['results'] += '<p>' + r['snippet'] + '</h3>'
        c['results'] += '<p>Posted ' + r['formattedRelativeTime'] + '</p>'
        c['results'] += '<a href="' + r['url'] + '">See original posting</a>'
        c['results'] += '</div>'
    c['success'] = 'true'
    c['total_results'] = json_decoded['totalResults']
    return HttpResponse(json.dumps(c), mimetype="application/json")
    