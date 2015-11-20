from django.contrib.auth.models import User
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

class Problem(BaseModel):
    name = models.CharField(max_length=100)
    discription = models.TextField()
    input_guide = models.TextField()
    output_guide = models.TextField()
    input_example = models.TextField()
    output_example = models.TextField()
    source = models.CharField(max_length=100, default='')
    hint = models.TextField(default='')
    time_limit = models.PositiveIntegerField(default=1000) #in ms
    memory_limit = models.PositiveIntegerField(default=64000) # in kB
    output_limit = models.PositiveIntegerField(default=1000) # in kB
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publish_at = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(User, null=True, blank=True)

class Language(BaseModel):
    name = models.CharField(max_length=20)

class StandardCode(BaseModel):
    problem = models.ForeignKey(Problem)
    language = models.ForeignKey(Language)
    code = models.TextField()
    editor = models.ForeignKey(User, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Submission(BaseModel):
    PENDING = 'p'
    RUNNING = 'r'
    AC = 'a'
    TLE = 't'
    MLE = 'm'
    OLE = 'o'
    WA = 'w'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (RUNNING, 'Running'),
        (AC, 'Accepted'),
        (TLE, 'Time Limit Exceed'),
        (MLE, 'Memory Limit Exceed'),
        (OLE, 'Output Limit Exceed'),
        (WA, 'Wrong Answer'),
    )

    problem = models.ForeignKey(Problem)
    user = models.ForeignKey(User)
    language = models.ForeignKey(Language)
    run_at = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    runtime_time = models.PositiveIntegerField(default=0)
    runtime_memory = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TestCase(BaseModel):
    problem = models.ForeignKey(Problem)
    editor = models.ForeignKey(User)
    input_data = models.TextField()
    output_data = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(BaseModel):
    FEMALE = 'f'
    MALE = 'm'
    UNKNOWN = 'u'
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (UNKNOWN, 'Unknown'),
    )

    user = models.OneToOneField(User)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
            default=UNKNOWN)
    school = models.CharField(max_length=50)
    prefer_language = models.ForeignKey(Language)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
