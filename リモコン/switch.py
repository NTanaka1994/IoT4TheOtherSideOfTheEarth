import socket
import RPi.GPIO as GPIO

RIGHT = 3
LEFT = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT, GPIO.IN)
GPIO.setup(RIGHT, GPIO.IN)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = ""
    if GPIO.input(LEFT):
        msg = "1"
    else:
        msg = "0"
    msg = msg + ","
    if GPIO.input(RIGHT):
        msg = msg + "1"
    else:
        msg = msg + "0"

    sock.sendto(msg.encode("utf-8"), ("10.153.229.254", 9999))
