from django.http import HttpResponse

#Returns an httpRepsonse object that has been instantiated with the text "Hello World"

def hello(request):
	return HttpResponse("Hello World")

def my_homepage_view(request):
	return HttpResponse("This is my homepage!")
