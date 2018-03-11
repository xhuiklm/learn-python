from . import views
from django.urls import path
urlpatterns = [
    path(r'',views.list),
]