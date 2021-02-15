from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_view(request):
    print("request  ---->>>  ", request, dir(request))
    return HttpResponse("hello this is demo ")


def index(request):
    if request.method == 'POST':
        return render(request, 'index.html', status=200)
    if request.method == 'GET':
        return HttpResponse("this get method ")
