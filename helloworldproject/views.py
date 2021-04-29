from django.http import HttpResponse

def hellorworldfunc(request):
  responseobject = HttpResponse('<h1>hello world</h1>')
  return responseobject
