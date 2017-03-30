from __future__ import unicode_literals

from django.db import models

class name(models.Model):
    name_text = models.CharField(max_length=200)
    # this is a character field defined as max length of 200
    pub_date = models.DateTimeField('date published')
    # this is an automated date stamp with the date published title
    def __str__(self):
        return self.name_text

class location(models.Model):
    location_text = models.CharField(max_length=200)
    # this is a character field defined as max length of 200
    pub_date = models.DateTimeField('date published')
    # this is an automated date stamp with the date published title
    def __str__(self):
        return self.location_text

class age(models.Model):
    age_text = models.CharField(max_length=3)
    # this is a character field defined as max length of 200
    pub_date = models.DateTimeField('date published')
    # this is an automated date stamp with the date published title
    def __str__(self):
        return self.age_text
