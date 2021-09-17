import socket
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.116", 1025))
s.listen(2)

print("Server on!")


while True:
    clt1, adr = s.accept()
    print(f"Connectedd to {adr}")

    clt1.send(bytes("socket programming in py", "utf-8"))

    clt2, adr2 = s.accept()

    print(f"Connectedd to " + str(adr2))

    clt2.send(bytes("socket programming in py", "utf-8"))

    class clt1m(Thread):
        def run(self):
            while True:
                message = clt1.recv(1024)
                m = message.decode("utf-8")
                print('user1: ' + m)
                clt2.send(bytes(m, "utf-8"))

    class clt2m(Thread):
        def run(self):
            while True:
                answer = clt2.recv(1024)
                an = answer.decode("utf-8")
                print('user2: ' + an)
                clt1.send(bytes(an, "utf-8"))

while True:
    client1_messages = clt1m()
    client2_messages = clt2m()

    client1_messages.start()
    client2_messages.start()
