from __future__ import unicode_literals

from django.db import models


# this would be a user id store
class name(models.Model):
    name = models.CharField(max_length=200)
    #name text
    location = models.CharField(max_length=200)
    #location text
    age = models.CharField(max_length=3)
    # this is a character field defined as max length of 200
    pub_date = models.DateTimeField('date published')
    # this is an automated date stamp with the date published title
    def __str__(self):
        return self.name


# this is a model of the data going into the database
