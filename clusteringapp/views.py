from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

#Returns an httpRepsonse object that has been instantiated with the text "Hello World"

def hello(request):
	return HttpResponse("Hello World")

def my_homepage_view(request):
	return HttpResponse("This is my homepage!")

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
