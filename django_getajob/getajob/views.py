from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
def index(request):
    return render_to_response('TemplateH/Pprincipal.html')
def post(request):
    return render_to_response('TemplateH/Publics.html')

# Create your views here.
