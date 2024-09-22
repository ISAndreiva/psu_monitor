
# Create your views here.
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import PSU_serial, PSU_base
import datetime

class IndexView(generic.ListView):
    template_name = 'psu/index.html'
    context_object_name = 'psu_list'

    def get_queryset(self):
        return PSU_base.objects.all()


def get_psu(request, pk):
    psu = get_object_or_404(PSU_base, pk=pk)
    return JsonResponse({
        'last_updated': int(psu.last_updated.timestamp()),
        'name': psu.name,
        'voltageIN': psu.get_voltageIN(),
        'currentIN': psu.get_currentIN(),
        'powerIN': psu.get_powerIN(),
        'voltageOUT': psu.get_voltageOUT(),
        'currentOUT': psu.get_currentOUT(),
        'powerOUT': psu.get_powerOUT(),
        'efficiency': psu.get_efficiency(),
        'temperature1': psu.get_temperature1(),
        'temperature2': psu.get_temperature2(),
        'temperature3': psu.get_temperature3(),
        'fan_speed': psu.get_fan_speed()
    })