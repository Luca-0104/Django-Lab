from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, 'hello.html', {'name' : 'Lucas'})