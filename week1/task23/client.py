p = int(input("Enter the port of the socket to connect to: "))

# Example taken from: https://www.geeksforgeeks.org/socket-programming-python/
# Import socket module
import socket

# Create a socket object
s = socket.socket()

# connect to the server on local computer
s.connect(('127.0.0.1', p))

# receive data from the server and decoding to get the string.
print ("Data received from remote socket: '" + s.recv(1024).decode() + "'")
# close the connection
s.close()   
