from django.shortcuts import render
from django.views.generic import ListView

from django.contrib.auth.models import User
from app.models import Problem

class ProblemList(ListView):
    model = Problem

class UserList(ListView):
    model = User
