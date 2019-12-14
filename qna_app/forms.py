from django import forms
from .models import QuestionModel, AnswerModel


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = "__all__"


class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = "__all__"
