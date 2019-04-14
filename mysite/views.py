from django.http import HttpResponse,Http404
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("<html><body>Hello World!</body></html>")
	
def current_time(request):
    now = datetime.datetime.now()
    html_text = "<html><body>It is now %s.</body></html>"% now
    return HttpResponse(html_text)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    ahead_time = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html_text = "<html><body>In %s hour(s) ,it will be %s.</body></html>"% (offset,ahead_time)
    return HttpResponse(html_text)
	
	
def index(request):
    return render(request,'index.html')

def test(request,page):
    htmlReturn = page+'.html'
    return render(request,htmlReturn)