# Generated by Django 5.1.2 on 2024-11-24 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('lectures', '0005_alter_lecture_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='course.course'),
        ),
    ]
