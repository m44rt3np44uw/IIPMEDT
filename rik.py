import serial
import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)
a = 0

coil_A_1_pin = 26
coil_A_2_pin = 13
coil_B_1_pin = 6
coil_B_2_pin = 5

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

sequence = ['1000', '0100', '0010', '0001']


def set_step(step):
        GPIO.output(coil_A_1_pin, step[0] == '1')
        GPIO.output(coil_A_2_pin, step[1] == '1')
        GPIO.output(coil_B_1_pin, step[2] == '1')
        GPIO.output(coil_B_2_pin, step[3] == '1')


def down(amount_of_steps):
        for i in range(amount_of_steps):
            for step in sequence:
                set_step(step)
                time.sleep(0.005)
                
if os.path.exists("/dev/ttyACM0"):
    ACM = '/dev/ttyACM0'
if os.path.exists("/dev/ttyACM1"):
    ACM = '/dev/ttyACM1'
if os.path.exists("/dev/ttyACM2"):
    ACM = '/dev/ttyACM2'
if os.path.exists("/dev/ttyACM3"):
    ACM = '/dev/ttyACM3'


ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    button = GPIO.input(2)
    read_serial = ser.readline()
    
    try:
        if 0 < int(read_serial) < 30:
            print("Brood")
        
        elif 30 < int(read_serial) < 60:
            print("Sinaasappel")
        
        elif 60 < int(read_serial) < 90:

            print("Banaan")

        else:
            print(read_serial)
    except:
        pass

    if not button:
        a = int(read_serial)
        set_step('0000')
        delay = 5
        steps = a
        down(int(steps)) 
        
    print("Product = {}".format(a))