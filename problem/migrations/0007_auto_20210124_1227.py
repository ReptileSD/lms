# Generated by Django 3.1.3 on 2021-01-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('problem', '0006_auto_20210122_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='cats_material_url',
            field=models.URLField(default='./static/problem_text-cpid-4942435.html'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='type',
            field=models.CharField(choices=[('CW', 'classwork'), ('HW', 'homework')], default='CW', max_length=2),
        ),
    ]