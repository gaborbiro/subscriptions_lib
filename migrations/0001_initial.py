# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('favicon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions_lib.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(upload_to='subscription_thumbnails/')),
                ('reference', models.CharField(blank=True, max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions_lib.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions_lib.Company')),
            ],
        ),
    ]
