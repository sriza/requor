from django.shortcuts import render
from .models import  QuestionModel,AnswerModel

# Create your views here.

def addquestion(request):
    question=QuestionModel.objects.all()
    return render(request,'newquestion.html',{'question':question})
