import RPi.GPIO as GPIO
import dht11
import time
import datetime
import pigpio
import requests

GPIO_RX = 18
BAUD = 9600
pi = pigpio.pi()
pi.bb_serial_read_open(GPIO_RX, BAUD, 8)
if not pi.connected:
    raise SystemExit("EXIT")

def nmea_to_deciaml(coord, direction):
    degrees = float(coord[:2])
    minutes = float(coord[2:])
    decimal = degrees + minutes / 60.0
    if direction in ["S", "W"]:
        decimal *= -1
    return decimal

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)
dic = {}
ido = 0
kei = 0
try:
    buf = b""
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
        count, data = pi.bb_serial_read(GPIO_RX)
        if count > 0:
            buf += data
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                s = line.decode("ascii", errors="ignore").strip()
                if s.startswith("$GPGGA"):
                    parts = s.split(",")
                    if len(parts) > 5 and parts[2] and parts[4]:
                        ido = nmea_to_deciaml(parts[2], parts[3])
                        kei = nmea_to_deciaml(parts[4], parts[5])
        #print("ido:%f, kei=%f"%(ido, kei))
        dic["hum"] = result.humidity
        dic["tmp"] = result.temperature
        dic["co2"] = 700
        dic["ido"] = ido
        dic["kei"] = kei
        #print(dic)
        if dic["hum"] != 0:
            requests.post("http://10.153.229.254/input-sensor",data=dic)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
finally:
    pi.bb_serial_read_close(GPIO_RX)
    pi.stop