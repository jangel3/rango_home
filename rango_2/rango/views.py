from django.shortcuts import render

# Create your views here.
context_dict = {'boldmessage': "I am a bold context message"}


def index(request):
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')
