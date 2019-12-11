from django import forms
from .models import QuestionModel,AnswerModel

class  QuestionForm(forms.ModelForm):
    class Meta:
        model= QuestionModel
        fields='__all__'
        
