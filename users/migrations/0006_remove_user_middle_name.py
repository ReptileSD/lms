# Generated by Django 3.2.15 on 2022-10-29 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_studygroup_user_study_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
    ]