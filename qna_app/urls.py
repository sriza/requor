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
    avote,
    adelete,
    update_answer,
    readmore,
    rvote,
)

urlpatterns = [
    path("addquestion/", addquestion, name="addquestion"),
    path("popular/", popular, name="popularquestions"),
    path("aupdate/<int:id>/", update_answer, name="aupdate"),
    path("update/<int:id>/", update_question, name="update"),
    path("question/", question, name="question"),
    path("delete/<int:id>/", delete, name="delete"),
    path("adelete/<int:id>/", adelete, name="adelete"),
    path("create/", QuestionModelCreateView.as_view(), name="create"),
    path("list/", QuestionModelListView.as_view(), name="list"),
    path("vote/<int:id>/", vote, name="vote"),
    path("avote/<int:id>/", avote, name="avote"),
    path("rvote/<int:id>/", rvote, name="rvote"),
    path("question/comment/", comment, name="comment"),
    path("readmore/<int:id>/", readmore, name="readmore"),
]
