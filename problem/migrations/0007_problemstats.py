# Generated by Django 3.1.8 on 2021-05-24 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0006_merge_20210517_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('green', models.IntegerField()),
                ('yellow', models.IntegerField()),
                ('red', models.IntegerField()),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='problem.problem')),
            ],
        ),
    ]
