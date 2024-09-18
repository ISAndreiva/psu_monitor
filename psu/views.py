
# Create your views here.
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import PSU_serial, PSU_base


class IndexView(generic.ListView):
    template_name = 'psu/index.html'
    context_object_name = 'psu_list'

    def get_queryset(self):
        return PSU_base.objects.all()

