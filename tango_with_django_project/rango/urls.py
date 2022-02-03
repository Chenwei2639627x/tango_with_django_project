from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    #<a href='/rango/about/'>About</a>,
    path(r'rango/about/', views.about, name='about'),
    path(r'rango/', views.index, name='index'),
]