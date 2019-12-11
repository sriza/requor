# Generated by Django 2.2 on 2019-12-11 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('posted_by', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question_desc', models.TextField()),
                ('question_img', models.ImageField(upload_to='QuestionImg')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_by', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField()),
                ('is_accepted', models.BooleanField()),
                ('answer_desc', models.TextField()),
                ('answer_img', models.ImageField(upload_to='AnswerImg')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna_app.QuestionModel')),
            ],
        ),
    ]