from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    
    return HttpResponse("This is About Us Page")

def problem_statement(request):
    return render(request, 'services.html')