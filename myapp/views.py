from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Alex")

def post_list(request):
    return render(request, 'myapp/post_list.html', {})