from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('homee/', views.home),
    # path('name/', views.name),
    # path('contant/', views.contant), 
    # path('about/', views.about),
    path('', include('myapp.urls')),
]

