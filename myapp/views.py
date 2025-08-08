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


def home(request):
    return HttpResponse("This is home page")


def help(request):
    return HttpResponse("This is help page")


def name(request,name):
    return HttpResponse(f"My name is : {name}")

def number(request, number):
    return HttpResponse(f"The number is: {number}")


def string(request, string):
    return HttpResponse(f"The string is: {string}")


def even_odd(request, num):
    if num % 2 == 0:
        return HttpResponse(f"{num} is even")
    else:
        return HttpResponse(f"{num} is odd")

