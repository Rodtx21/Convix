import socket
from threading import *

def get_string(r):
    a = input(r)

    while (True):
        if (isinstance(a, str) or isinstance(a, int)):
            return str(a)
        else:
            a = input(r)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.116", 1025))

msg = s.recv(1024)
print(msg.decode("utf-8"))

class sending(Thread):
    def run(self):
        while True:
            m = get_string("")
            s.send(bytes(m, "utf-8"))

class receiving(Thread):
    def run(self):
        while True:
            answer = s.recv(1024)
            an = answer.decode("utf-8")
            print(an)

while True:
    send = sending()
    recei = receiving()

    send.start()
    recei.start()
