# Generated by Django 3.1.3 on 2021-01-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cathie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatsUserLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='CourseContestLink',
        ),
        migrations.DeleteModel(
            name='UsersLink',
        ),
    ]
