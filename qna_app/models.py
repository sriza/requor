from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_desc = models.TextField()
    question_votes = models.IntegerField(default=0)
    question_img = models.ImageField(upload_to="QuestionImg", blank=True, null=True)

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    # objects=models.Manager() #grey box in object

    def __str__(self):
        return self.title


class AnswerModel(models.Model):
    ans_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    ans_votes = models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=0)
    answer_desc = models.TextField()
    answer_img = models.ImageField(upload_to="AnswerImg", blank=True, null=True)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_desc

