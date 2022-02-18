from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    #<a href='/rango/about/'>About</a>,
    path(r'rango/about/', views.about, name='about'),
    path(r'rango/', views.index, name='index'),
    path('', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'rango/category/<slug:category_name_slug>/',views.show_category, name='show_category'),
]