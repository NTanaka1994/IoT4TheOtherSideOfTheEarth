import socket
import json

UDP_HOST = "0.0.0.0"
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_HOST, UDP_PORT)) 
print("start")
while True:
    try:
        data, addr = sock.recvfrom(65535)
        dic = {}
        try:
            text = data.decode("utf-8").split(",")
            dic["left"] = int(text[0])
            dic["right"] = int(text[1])
        except:
            dic["left"] = 0
            dic["right"] = 0
        f = open("control.json", "w", encoding="utf-8")
        f.write(json.dumps(dic))
        f.close()
    except:
        _ = 0
