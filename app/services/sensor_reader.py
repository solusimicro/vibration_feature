import socket
import json
import threading

LATEST_WINDOW = {}

def start_sensor_reader(host="127.0.0.1", port=7000):
    global LATEST_WINDOW

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    buffer = b""

    while True:
        buffer += sock.recv(8192)
        if b"\n" in buffer:
            line, buffer = buffer.split(b"\n", 1)
            LATEST_WINDOW = json.loads(line.decode())
