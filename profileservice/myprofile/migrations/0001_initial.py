# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=100, verbose_name='Profiss\xe3o')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
            ],
        ),
    ]