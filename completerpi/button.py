import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to  

try:
    while True:
         button_state = GPIO.input(18)
         print(button_state)
         if button_state == False: 
              print('Button Pre/ssed...') 
#          else:
#              print(button_state)
except:
    GPIO.cleanup()