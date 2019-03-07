import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.0.70' #----------------wlan0
port = 50000
address = (ip, port)

server.bind((address))
server.listen(1)

print ('Listening on MI5 servers ' + str(address))

conn, addr = server.accept()

print ('Connected to 007: ' + str(addr[0]) + ': ' + str(addr[1]))

while 1:
    data = conn.recv(1024)

    print ('received ' + str(data))

    if (data == 'occupied'):
    	print ('this would work')
    if not data:
        break
    conn.sendall(data)
conn.close()