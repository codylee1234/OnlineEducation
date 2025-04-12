# Generated by Django 2.0.7 on 2018-07-30 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20180730_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='points',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='教学特点'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='work_company',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='就职公司'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='work_position',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='公司职位'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='work_years',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='工作年限'),
        ),
    ]
