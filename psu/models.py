from polymorphic.models import PolymorphicModel
from django.db import models
import serial
import random



class PSU_base(PolymorphicModel):
    name = models.CharField(max_length=200)

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_data()


    def __str__(self):
        return str(self.name) + " (" + str(self.serial) + ")"

    def update_data(self):
        try:
            ser = serial.Serial(self.serial, 115200, timeout=1)
            first_line = ser.readline()
            if first_line == b'':
                raise serial.SerialException
            while first_line != b'Begin transmission\r\n':
                first_line = ser.readline()
            self.currentIN = float(ser.readline())
            self.voltageIN = float(ser.readline())
            self.powerIN = float(ser.readline())
            self.currentOUT = float(ser.readline())
            self.voltageOUT = float(ser.readline())
            self.powerOUT = float(ser.readline())
            self.fan_speed = float(ser.readline())
            self.temperature1 = float(ser.readline())
            self.temperature2 = float(ser.readline())
            self.temperature3 = float(ser.readline())
            if ser.readline() != b'End transmission\r\n':
                raise serial.SerialException
            ser.close()

        except serial.SerialException:
            self.currentIN = "Error"
            self.voltageIN = "Error"
            self.powerIN = "Error"
            self.currentOUT = "Error"
            self.voltageOUT = "Error"
            self.powerOUT = "Error"
            self.temperature1 = "Error"
            self.temperature2 = "Error"
            self.temperature3 = "Error"
            self.fan_speed = "Error"


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