# Generated by Django 2.2 on 2019-12-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answermodel',
            name='answer_img',
            field=models.ImageField(blank=True, null=True, upload_to='AnswerImg'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='question_img',
            field=models.ImageField(blank=True, null=True, upload_to='QuestionImg'),
        ),
    ]