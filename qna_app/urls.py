from django.urls import path
from .views import (
    addquestion,
    popular,
    question,
    update_question,
    delete,
    QuestionModelCreateView,
    QuestionModelListView,
    vote,
    comment,
)

urlpatterns = [
    path("addquestion/", addquestion, name="addquestion"),
    path("popular/", popular, name="popularquestions"),
    path("update/<int:id>/", update_question, name="update"),
    path("question/", question, name="question"),
    path("delete/<int:id>/", delete, name="delete"),
    path("create/", QuestionModelCreateView.as_view(), name="create"),
    path("list/", QuestionModelListView.as_view(), name="list"),
    path("vote/<int:id>/", vote, name="vote"),
    path("question/comment/", comment, name="comment"),
]
