from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User

from django.db import models

# Create your models here.


class Playground(models.Model):
    user = models.ForeignKey(User, default=1)
    name_playground = models.CharField(max_length=20)
    description_playground = models.CharField(max_length=50)
    kind_of_sport = models.CharField(max_length=100, default=False)
    Location_playground = models.CharField(max_length=10)
    review_playground = models.IntegerField(default=1)  # default should be zero
    created_update = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_now = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name_playground


class Event(models.Model):
    playground = models.ForeignKey(Playground, default=1)
    event_name = models.CharField(max_length=50)
    event_instructions = models.TextField()
    event_review = models.IntegerField(default=1)  # default should be zero
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    created_update = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_now = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.event_instructions


class Pastevent(models.Model):
    playground = models.ForeignKey(Playground, default=1)
    event_name = models.ForeignKey(Event, default=1)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.describetion
