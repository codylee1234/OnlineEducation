# Generated by Django 2.0.7 on 2018-08-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
    ]
