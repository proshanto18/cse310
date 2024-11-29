# Generated by Django 5.1.2 on 2024-11-29 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0006_alter_lecture_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_file', models.FileField(help_text='Upload a text file containing the question.', upload_to='exercises/questions/')),
                ('answer_file', models.FileField(help_text='Upload a text file containing the answer code.', upload_to='exercises/answers/')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='lectures.lecture')),
            ],
        ),
    ]