# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('useremail', models.EmailField(max_length=250, null=True)),
                ('password', models.CharField(max_length=250, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isSupportEngineer', models.BooleanField(default=False)),
                ('isClient', models.BooleanField(default=False)),
            ],
        ),
    ]
