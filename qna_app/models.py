from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    title=models.CharField(max_length=255)
    posted_by=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    question_desc=models.TextField()
    question_img=models.ImageField(upload_to="QuestionImg")


class AnswerModel(models.Model):
    ans_by=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    votes=models.IntegerField()
    is_accepted=models.BooleanField()
    answer_desc=models.TextField()
    answer_img=models.ImageField(upload_to="AnswerImg")
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)




