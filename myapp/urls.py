from . import views
from django.urls import path

urlpatterns = [
    path('index', views.home),
    path('data', views.data),
    # path('even_odd/<int:number>', views.even_odd),
    path('even_odd', views.even_odd),
    path('html/', views.htmlfile),
    path('data_file/', views.datafile),
]