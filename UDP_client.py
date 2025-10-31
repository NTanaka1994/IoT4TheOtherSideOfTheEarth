import socket
import time

UDP_IP = "10.111.135.135"   # 例: "192.168.0.10"
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 左ボタンが押されている場合1、右ボタンが押されていない場合0（例）
    # 実際にはGPIO入力から値を取る
    left = input("左ボタン(1/0): ")
    right = input("右ボタン(1/0): ")

    message = str(left) + "," + str(right)
    sock.sendto(message.encode("utf-8"), (UDP_IP, UDP_PORT))
    print(f"送信: {message}")

    time.sleep(0.2)  # 200ms間隔で送信
