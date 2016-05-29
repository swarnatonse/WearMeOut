#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = 'LAPTOP-PBTV9SHU'
print(host)
port = 12345                # Reserve a port for your service.

s.connect((host, port))
s.send('Casual'.encode('utf-8'))
print(s.recv(1024).decode('utf-8'))
s.close                     # Close the socket when done
