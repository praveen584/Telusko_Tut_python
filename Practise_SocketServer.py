import socket

s = socket.socket()
print('Conn created')

s.bind(('localhost',9999))

s.listen(3)
print('Waiting for connections')

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print(f'Connected with {addr} and {name}')

    c.send(bytes('Welcome to Python Programming','utf-8'))

    c.close()