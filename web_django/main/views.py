from django.shortcuts import render
from django.http import HttpResponse

def index_views(request):
	return HttpResponse("main index")
