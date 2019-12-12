from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionModel, AnswerModel, CategoryModel
from .forms import QuestionForm
from django.http import HttpResponse

# Create your views here.


def addquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("Submitted")
            except:
                return HttpResponse("Failed")
        else:
            return HttpResponse(form.errors)

    else:
        form = QuestionForm
        # question = QuestionModel.objects.all()
        return render(request, "questionmodel_create.html", {"form": form})


def popular(request):
    question = QuestionModel.objects.filter(question_votes__gt=2)
    return render(request, "popular.html", {"question": question})


def question(request):
    question = QuestionModel.objects.all()
    return render(request, "questionmodel_list.html", {"question": question})


def update_question(request, id):
    question = get_object_or_404(QuestionModel, id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect("question")
            except:
                return HttpResponse("Failed")
        else:
            return HttpResponse(form.errors)

    else:
        form = QuestionForm(instance=question)
        # question = QuestionModel.objects.all()
        return render(request, "questionmodel_create.html", {"form": form})


def delete(request, id):
    QuestionModel.objects.get(id=id).delete()
    return HttpResponse("deleted")

