import requests
import time
while True:
    dic = {}
    dic["hum"] = 48
    dic["tmp"] = 30
    dic["co2"] = 500
    dic["ido"] = 35.709756
    dic["kei"] = 139.522493
    files = {'file': open("sample.jpg", "rb")}
    #req = requests.post("http://10.111.135.135/input-sensor", data=dic, files=files)
    req = requests.post("http://192.168.128.192/input-sensor", data=dic, files=files)
    time.sleep(0.5)