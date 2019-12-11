from django.urls import path
from .views import addquestion

urlpatterns = [
    path('addquestion/',addquestion,name="addquestion")  
]
