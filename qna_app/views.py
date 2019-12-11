from django.shortcuts import render
from .models import QuestionModel, AnswerModel, CategoryModel

# Create your views here.


def addquestion(request):
    question = QuestionModel.objects.all()
    return render(request, "newquestion.html", {"question": question})


def popular(request):
    question = QuestionModel.objects.filter(question_votes__gt=2)
    return render(request, "popular.html", {"question": question})
