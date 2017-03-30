from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from . import models # imports all the info from the models file


class IndexView(generic.ListView):
    template_name = 'savedata/savedataindex.html'
    context_object_name = 'latest_name_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return models.name.objects.order_by('-pub_date')[:5]
