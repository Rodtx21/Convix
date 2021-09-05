import socket

def get_string(r):
    a = input(r)

    while (True):
        if (isinstance(a, str) or isinstance(a, int)):
            return str(a)
        else:
            a = input(r)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("5.43.52.92", 1025))

msg = s.recv(1024)
print(msg.decode("utf-8"))

while True:
    answer = s.recv(1024)
    an = answer.decode("utf-8")
    print(an)
    
    m = get_string("")
    m = s.send(bytes(m, "utf-8"))