from django.urls import path
from .views import addquestion, popular, question, update_question, delete

urlpatterns = [
    path("addquestion/", addquestion, name="addquestion"),
    path("popular/", popular, name="popularquestions"),
    path("update/<int:id>/", update_question, name="update"),
    path("question/", question, name="question"),
    path("delete/<int:id>/", delete, name="delete"),
]
