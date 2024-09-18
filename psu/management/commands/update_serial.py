from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import PSU_serial
from time import sleep
import serial

class Command(BaseCommand):
    help = 'Update the serial data'

    def handle(self, *args, **options):
        while True:
            try:
                for psu in PSU_serial.objects.all():
                    try:
                        ser = serial.Serial(psu.serial, 115200, timeout=1)
                        first_line = ser.readline()
                        if first_line == b'':
                            raise serial.SerialException
                        while first_line != b'Begin transmission\r\n':
                            first_line = ser.readline()
                        psu.currentIN = float(ser.readline())
                        psu.voltageIN = float(ser.readline())
                        psu.powerIN = float(ser.readline())
                        psu.currentOUT = float(ser.readline())
                        psu.voltageOUT = float(ser.readline())
                        psu.powerOUT = float(ser.readline())
                        psu.fan_speed = float(ser.readline())
                        psu.temperature1 = float(ser.readline())
                        psu.temperature2 = float(ser.readline())
                        psu.temperature3 = float(ser.readline())
                        psu.last_updated = timezone.now()
                        if ser.readline() != b'End transmission\r\n':
                            raise serial.SerialException
                        ser.close()
                        psu.save()

                    except serial.SerialException:
                        psu.currentIN = -1
                        psu.voltageIN = -1
                        psu.powerIN = -1
                        psu.currentOUT = -1
                        psu.voltageOUT = -1
                        psu.powerOUT = -1
                        psu.temperature1 = -1
                        psu.temperature2 = -1
                        psu.temperature3 = -1
                        psu.fan_speed = -1
                        psu.last_updated = timezone.now()
                        psu.save()
                        self.stdout.write(self.style.ERROR(f'Error in serial communication with {psu.name}'))
                    sleep(1)
            except KeyboardInterrupt:
                break
