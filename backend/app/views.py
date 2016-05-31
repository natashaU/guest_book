from django.shortcuts import render

# Create your views here.
def index(request):
  foo = request.GET.get('first_name')
  bar = request.GET.get('last_name')
  context = {
    "baz": foo,
    "bat": bar
  }
  return render(request, "index.html", context)
