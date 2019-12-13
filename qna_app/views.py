from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionModel, AnswerModel, CategoryModel
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

# Create your views here.


class QuestionModelCreateView(CreateView):
    model = QuestionModel
    fields = "__all__"


class QuestionModelListView(ListView):
    model = QuestionModel
    queryset = QuestionModel.objects.all()


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
        category = CategoryModel.objects.all()
        # question = QuestionModel.objects.all()
        return render(request, "questionmodel_create.html", {"category": category})


def popular(request):
    question = QuestionModel.objects.filter(question_votes__gt=2)
    return render(request, "popular.html", {"question": question})


def question(request):
    question = QuestionModel.objects.all()
    answers = AnswerModel.objects.all()
    return render(
        request, "questionmodel_list.html", {"questions": question, "answer": answers}
    )


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
        category = CategoryModel.objects.all()
        return render(
            request, "questionmodel_create.html", {"category": category, "form": form}
        )


def delete(request, id):
    try:
        QuestionModel.objects.get(id=id).delete()
        return redirect("question")
    except:
        return HttpResponse(" deletion failed")


def vote(request, id):
    question = QuestionModel.objects.get(id=id)
    question.question_votes += 1
    question.save()
    return redirect("question")


def comment(request):
    if request.method == "POST":
        form = AnswerForm(request.POST, request.FILES)
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
        category = CategoryModel.objects.all()
        return render(
            request, "questionmodel_create.html", {"category": category, "form": form}
        )


def update_answer(request, id):
    ans = get_object_or_404(AnswerModel, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST, request.FILES, instance=ans)
        if form.is_valid():
            try:
                form.save()
                return redirect("question")
            except:
                return HttpResponse("Failed")
        else:
            return HttpResponse(form.errors)

    else:
        form = AnswerForm(instance=ans)
        question = QuestionModel.objects.all()
        answers = AnswerModel.objects.all()
        # question = QuestionModel.objects.all()
        return render(
            request,
            "questionmodel_list.html",
            {"questions": question, "answer": answers, "form": form},
        )


def adelete(request, id):
    try:
        AnswerModel.objects.get(id=id).delete()
        return redirect("question")
    except:
        return HttpResponse(" deletion failed")


def avote(request, id):
    ans = AnswerModel.objects.get(id=id)
    ans.ans_votes += 1
    ans.save()
    return redirect("question")


def rvote(request, id):
    ans = AnswerModel.objects.get(id=id)
    ans.ans_votes += 1
    ans.save()
    return redirect("readmore")


def readmore(request, id):
    que = QuestionModel.objects.get(id=id)
    ans = AnswerModel.objects.filter(question=id)
    return render(
        request, "questionmodel_details.html", {"question": que, "answer": ans}
    )

