from . import views
from django.urls import path
urlpatterns = [
    path(r'',views.index,name='index'),  
     path(r'contact',views.contact,name='contact')
]