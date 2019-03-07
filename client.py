import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.0.70', 50000))

busy = 'occupied'

client.sendall(busy.encode('utf-8'))

data = client.recv(1024)

client.close()

print ('Received ' + repr(data))
