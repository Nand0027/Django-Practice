from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse("This is home page")

def data(request):
    data = {
        "name": "John Doe",
        "age": 25,
        "city": "New York"
    }
    return JsonResponse(data)

# def even_odd(request, number):
def even_odd(request):
    number = 47
    if number % 2 == 0:
        return HttpResponse(f"{number} is even")
    else:
        return HttpResponse(f"{number} is odd")
    
    
def htmlfile(request):  
        return render(request, 'index.html')


def datafile(request):
    a = "Django is a framework"
    return render(request, 'index.html', {'data': a})