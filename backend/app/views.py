from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  landing_page_content = "<html><body>hello world welcome to my page!</body></html>"
  my_response = HttpResponse(landing_page_content)
  return my_response
