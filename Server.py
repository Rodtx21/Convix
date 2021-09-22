import socket
import threading

host = "192.168.1.71"
port = 7037
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)

print("Server on!")

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            break

def receive():
    while True:
        client, adress = s.accept()
        print(f"Connected with {str(adress)}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode("utf-8"))
        client.send('Connected to the server!'.encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        threading.start()

print("Server is listening!")
receive()

#while True:
 #  print(f"Connectedd to {adr}")
#
 #   clt1.send(bytes("socket programming in py", "utf-8"))
#
 #   clt2, adr2 = s.accept()
#
 #   print(f"Connectedd to " + str(adr2))
#
 #   clt2.send(bytes("socket programming in py", "utf-8"))
#
 #   class clt1m(Thread):
  #      def run(self):
   #         while True:
    #            message = clt1.recv(1024)
     #           m = message.decode("utf-8")
      ##          print('user1: ' + m)
        #        clt2.send(bytes(m, "utf-8"))
#
 #   class clt2m(Thread):
#        def run(self):
 #           while True:
#                answer = clt2.recv(1024)
#                an = answer.decode("utf-8")
#                print('user2: ' + an)
#                clt1.send(bytes(an, "utf-8"))

#while True:
#    client1_messages = clt1m()
#    client2_messages = clt2m()
#
 #   client1_messages.start()
 #   client2_messages.start()
