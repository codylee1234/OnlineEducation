# Generated by Django 2.0.7 on 2018-08-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20180731_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]
