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
    if "id" in request.session:
        question = QuestionModel.objects.all()
        answers = AnswerModel.objects.all()
        return render(
            request,
            "questionmodel_list.html",
            {"questions": question, "answer": answers,},
        )
    else:
        return redirect("login")


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


def rcomment(request, id):
    if request.method == "POST":
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                url = "/qna/readmore/" + str(id)
                return redirect(url)
            except:
                return HttpResponse("Failed")
        else:
            return HttpResponse(form.errors)


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


def update_answer(request, id):
    ans = get_object_or_404(AnswerModel, id=id)

    if request.method == "POST":
        que = QuestionModel.objects.get(title=ans.question)
        form = AnswerForm(request.POST, request.FILES, instance=ans)
        if form.is_valid():
            try:
                form.save()
                url = "/qna/readmore/" + str(que.id)
                return redirect(url)
            except:
                return HttpResponse("Failed")
        else:
            return HttpResponse(form.errors)

    else:
        form = AnswerForm(instance=ans)
        # question = QuestionModel.objects.all()
        return render(
            request, "questionmodel_details.html", {"question": question, "form": form}
        )


def adelete(request, id):
    try:
        ans = AnswerModel.objects.get(id=id)
        que = QuestionModel.objects.get(title=ans.question)
        AnswerModel.objects.get(id=id).delete()
        url = "/qna/readmore/" + str(que.id)
        return redirect(url)
    except:
        return HttpResponse("deletion failed")


def avote(request, id):
    ans = AnswerModel.objects.get(id=id)
    que = QuestionModel.objects.get(title=ans.question)
    ans.ans_votes += 1
    ans.save()
    url = "/qna/readmore/" + str(que.id)
    return redirect(url)


def rvote(request, id):
    question = QuestionModel.objects.get(id=id)
    question.question_votes += 1
    question.save()
    url = "/qna/readmore/" + str(question.id)
    return redirect(url)


def readmore(request, id):
    que = QuestionModel.objects.get(id=id)
    ans = AnswerModel.objects.filter(question=id)
    question = QuestionModel.objects.filter(question_votes__gt=12)
    return render(
        request,
        "questionmodel_details.html",
        {"question": que, "answer": ans, "questions": question},
    )


# random


def test(request):
    question = QuestionModel.objects.all()
    answers = AnswerModel.objects.all()
    return render(request, "test.html", {"questions": question, "answer": answers,})


def random(request):
    question = QuestionModel.objects.filter(category=1)
    return render(request, "questionmodel_list.html", {"questions": question})


def health(request):
    question = QuestionModel.objects.filter(category=2)
    return render(request, "questionmodel_list.html", {"questions": question})


def science(request):
    question = QuestionModel.objects.filter(category=3)
    return render(request, "questionmodel_list.html", {"questions": question})

