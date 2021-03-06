'''
An HTTP Request in Python
    - The example below shows the full lifecycle of an HTTP request
    - socket, connect, encode, send, receive, decode, close
'''
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# Bytes properly encoded in UTF-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# Sending the bytes out with cmd
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()