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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('input_guide', models.TextField()),
                ('output_guide', models.TextField()),
                ('input_example', models.TextField()),
                ('output_example', models.TextField()),
                ('source', models.CharField(default=b'', max_length=100)),
                ('hint', models.TextField(default=b'')),
                ('time_limit', models.PositiveIntegerField(default=1000)),
                ('memory_limit', models.PositiveIntegerField(default=64000)),
                ('output_limit', models.PositiveIntegerField(default=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publish_at', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(default=b'u', max_length=1, choices=[(b'f', b'Female'), (b'm', b'Male'), (b'u', b'Unknown')])),
                ('school', models.CharField(max_length=50)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('editor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_at', models.DateTimeField(auto_now_add=True)),
                ('code', models.TextField()),
                ('runtime_time', models.PositiveIntegerField(default=0)),
                ('runtime_memory', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(max_length=1, choices=[(b'p', b'Pending'), (b'r', b'Running'), (b'a', b'Accepted'), (b't', b'Time Limit Exceed'), (b'm', b'Memory Limit Exceed'), (b'o', b'Output Limit Exceed'), (b'w', b'Wrong Answer')])),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
