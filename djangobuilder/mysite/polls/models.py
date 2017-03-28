from __future__ import unicode_literals

from django.db import models

# this is a model for a question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # this is a character field defined as max length of 200
    pub_date = models.DateTimeField('date published')
    # this is an automated date stamp with the date published title
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # quetsion being saved with the foreignkey, when deleted everything is deleted also
    choice_text = models.CharField(max_length=200)
    # choice text char with max length of 200
    votes = models.IntegerField(default=0)
    # votes field with integer number, default is 0
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
