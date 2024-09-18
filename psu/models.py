from polymorphic.models import PolymorphicModel
from django.db import models
from django.utils import timezone
import random



class PSU_base(PolymorphicModel):
    name = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    
    def update_data(self):
        pass

    
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


class PSU_random(PSU_base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_data()


    def __str__(self):
        return str(self.name) + " (random)"

    def update_data(self):
        self.currentIN = random.uniform(0, 10)
        self.voltageIN = random.uniform(0, 10)
        self.powerIN = self.currentIN * self.voltageIN
        self.currentOUT = random.uniform(0, 10)
        self.voltageOUT = random.uniform(0, 10)
        self.powerOUT = self.currentOUT * self.voltageOUT
        self.temperature1 = random.uniform(0, 100)
        self.temperature2 = random.uniform(0, 100)
        self.temperature3 = random.uniform(0, 100)
        self.fan_speed = random.uniform(1000, 10000)
        self.last_updated = timezone.now()

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