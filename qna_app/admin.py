from django.contrib import admin
from .models import QuestionModel, AnswerModel, CategoryModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
