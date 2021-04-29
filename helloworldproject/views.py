from django.http import HttpResponse
from django.views.generic import TemplateView

def hellorworldfunc(request):
  responseobject = HttpResponse('<h1>hello world</h1>')
  return responseobject

class HelloWorldClass(TemplateView):
  template_name = 'hello.html'
