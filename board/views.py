from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader, Context
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
    results_start= request.GET.get('results_start', '')
    payload = {'publisher': '7575596370066104', 'v': '2', 'format': 'json', 'q': query, 'l': location, 'start' : results_start}
    r = requests.get('http://api.indeed.com/ads/apisearch', params=payload)
    json_decoded = r.json
    total_results = json_decoded['totalResults']
    end_results = json_decoded['end']
    if total_results == 0:
        c['results'] = 'No search results. Please Try again.'
        c['more_results'] = 'false'
    elif total_results == end_results:
        c['results'] = "There are no more results."
        c['more_results'] = 'false'
    else:
        t = loader.get_template('board/elements/job_block.html') 
        ci = Context({'results' : json_decoded['results']})
        c['results'] = t.render(ci)
        c['more_results'] = 'true'
    # iterate through results and parse html
    c['success'] = 'true'
    c['query'] = query
    c['location'] = location
    c['total_results'] = total_results
    c['results_end'] = end_results
    return HttpResponse(json.dumps(c), content_type="application/json")


# def search(request):
#     c = {}
#     query = request.GET.get('query', '')
#     location = request.GET.get('location', '')
#     results_start= request.GET.get('results_start', '')
#     payload = {'publisher': '7575596370066104', 'v': '2', 'format': 'json', 'q': query, 'l': location, 'start' : results_start}
#     r = requests.get('http://api.indeed.com/ads/apisearch', params=payload)
#     json_decoded = r.json
#     total_results = json_decoded['totalResults']
#     end_results = json_decode['end']
#     if total_results == 0:
#         c['results'] = 'No search results. Please Try again.'
#         c['more_results'] = 'false'
#     elif total_results == end_results:
#         c['results'] = "There are no more results."
#         c['more_results'] = 'false'
#     else:
#         c['results']= render_to_string('board/elements/job_block.html',json_decoded['results'])
#         c['more_results'] = 'true'
#     c['success'] = 'true'
#     c['query'] = query
#     c['location'] = location
#     c['total_results'] = total_results
#     c['results_end'] = end_results
#     return HttpResponse(json.dumps(c), mimetype="application/json")
    