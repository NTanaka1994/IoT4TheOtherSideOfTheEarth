import requests
import json
import RPi.GPIO as GPIO
#7と11

LEFT = 7
RIGHT = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEFT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIGHT, GPIO.OUT, initial=GPIO.LOW)

while True:
    res = requests.get("http://10.111.174.89/control")
    dic = json.loads(res)
    if dic["left"] == 1:
        GPIO.output(LEFT, GPIO.HIGH)
    else:
        GPIO.output(LEFT, GPIO.LOW)
    if dic["right"] == 1:
        GPIO.output(RIGHT, GPIO.HIGH)
    else:
        GPIO.output(RIGHT, GPIO.LOW)