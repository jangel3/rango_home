from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Rango says... hello world<br><a href='rango/about/'>about</a>")


def about(request):
    return HttpResponse('Rango says... this is the about page.<br><a href=\'/rango/\'>Home</a>')