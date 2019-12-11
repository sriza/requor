from django.urls import path
from .views import addquestion,popular

urlpatterns = [
    path('addquestion/',addquestion,name="addquestion"), 
    path('popular/',popular,name="popularquestions") 
]
