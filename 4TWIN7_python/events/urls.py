from .views import *
from django.urls import path

urlpatterns = [ #appel tt les url dans 
    path('', homePage,name="Home_Page"),
]
