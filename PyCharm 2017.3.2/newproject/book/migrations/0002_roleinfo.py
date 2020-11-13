# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-09-27 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=20, verbose_name='角色名字')),
                ('gender', models.SmallIntegerField(verbose_name='性别')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
    ]
