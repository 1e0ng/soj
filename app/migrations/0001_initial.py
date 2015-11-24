# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('supported', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('input_guide', models.TextField()),
                ('output_guide', models.TextField()),
                ('input_example', models.TextField()),
                ('output_example', models.TextField()),
                ('source', models.CharField(default='', max_length=100)),
                ('hint', models.TextField(default='')),
                ('time_limit', models.PositiveIntegerField(default=1000)),
                ('memory_limit', models.PositiveIntegerField(default=64000)),
                ('output_limit', models.PositiveIntegerField(default=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publish_at', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('f', 'Female'), ('m', 'Male'), ('u', 'Unknown')], default='u', max_length=1)),
                ('school', models.CharField(default='', max_length=50)),
                ('company', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prefer_language', models.ForeignKey(to='app.Language')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StandardCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('editor', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(to='app.Language')),
                ('problem', models.ForeignKey(to='app.Problem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_at', models.DateTimeField(auto_now_add=True)),
                ('code', models.TextField()),
                ('runtime_time', models.PositiveIntegerField(default=0)),
                ('runtime_memory', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('p', 'Pending'), ('r', 'Running'), ('a', 'Accepted'), ('t', 'Time Limit Exceed'), ('m', 'Memory Limit Exceed'), ('o', 'Output Limit Exceed'), ('w', 'Wrong Answer')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(to='app.Language')),
                ('problem', models.ForeignKey(to='app.Problem')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField()),
                ('output_data', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('problem', models.ForeignKey(to='app.Problem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
