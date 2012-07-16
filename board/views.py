from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
def home(request, template='board/home.html'):
    c = {}
    return render_to_response(template, c)
