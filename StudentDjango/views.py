from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Student Django application!")

def name(request):
    return HttpResponse("Anand Yadav")

def contant(request):
    return HttpResponse("This is the content page.")

def about(request):
    return HttpResponse("This is the about page.")