from polymorphic.models import PolymorphicModel
from django.db import models
from django.utils import timezone
import random



class PSU_base(PolymorphicModel):
    name = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
    def get_voltageIN(self):
        pass

    
    def get_voltageOUT(self):
        pass

    
    def get_currentIN(self):
        pass

    
    def get_currentOUT(self):
        pass

    
    def get_powerIN(self):
        pass

    
    def get_powerOUT(self):
        pass

    
    def get_efficiency(self):
        pass

    
    def get_temperature1(self):
        pass

    
    def get_temperature2(self):
        pass

    
    def get_temperature3(self):
        pass

    
    def get_fan_speed(self):
        pass

class PSU_serial(PSU_base):
    serial = models.CharField(max_length=200)
    currentIN = models.FloatField(default=-1)
    voltageIN = models.FloatField(default=-1)
    powerIN = models.FloatField(default=-1)
    currentOUT = models.FloatField(default=-1)
    voltageOUT = models.FloatField(default=-1)
    powerOUT = models.FloatField(default=-1)
    temperature1 = models.FloatField(default=-1)
    temperature2 = models.FloatField(default=-1)
    temperature3 = models.FloatField(default=-1)
    fan_speed = models.FloatField(default=-1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.name) + " (" + str(self.serial) + ")"

    def get_voltageIN(self):
        return self.voltageIN

    def get_voltageOUT(self):
        return self.voltageOUT

    def get_currentIN(self):
        return self.currentIN

    def get_currentOUT(self):
        return self.currentOUT

    def get_powerIN(self):
        return self.powerIN

    def get_powerOUT(self):
        return self.powerOUT

    def get_temperature1(self):
        return self.temperature1

    def get_temperature2(self):
        return self.temperature2

    def get_temperature3(self):
        return self.temperature3

    def get_fan_speed(self):
        return self.fan_speed
