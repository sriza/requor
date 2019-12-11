from django.urls import path,include
from qna_app.views import addquestion

urlpatterns = [
    path('add',addquestion,name="add"),
]
