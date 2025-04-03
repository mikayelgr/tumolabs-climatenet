# sample taken from https://www.geeksforgeeks.org/socket-programming-python/
import socket			 

# next create a socket object 
s = socket.socket()		 
print ("Socket successfully created")

port = 0 # this means that a port will be chosen automatically

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))		 
print ("socket binded to %s" % (s.getsockname()[1])) 

# put the socket into listening mode 
s.listen(5)	 
print ("socket is listening")		 

# a forever loop until we interrupt it or 
# an error occurs 
while True: 
    # Establish connection with client. 
    c, addr = s.accept()	 
    print ('Got connection from', addr )

    # send a thank you message to the client. encoding to send byte type. 
    c.send('Thank you for connecting'.encode()) 

    # Close the connection with the client 
    c.close()

    # Breaking once connection closed
    break

