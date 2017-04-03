from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    location = forms.CharField(max_length=200)
    age = forms.CharField(max_length=3)
    pub_date = forms.DateTimeField('date published')

# this is the data going in from the form
