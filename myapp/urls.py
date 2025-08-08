from . import views
from django.urls import path
from myapp.views import help,home,name,number,string,even_odd

urlpatterns = [
    path('index', views.home),
    path('data', views.data),
    # path('even_odd/<int:number>', views.even_odd),
    path('even_odd', views.even_odd),
    path('html/', views.htmlfile),
    path('data_file/', views.datafile),
    path('homee/',home),
    path('help/',help),
    path('user/<name>/', name),
    path('number/<int:number>/', number),
    path('string/<str:string>/', string),
    path('even_odd/<int:num>/', even_odd),
]