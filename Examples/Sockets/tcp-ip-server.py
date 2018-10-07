import socket
import sys

#Create TCP/IP Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding the Socket to the port
addr = ("localhost", 1000);
socket.bind(addr)

#Listen fo incoming connections
socket.listen(1)

while True:
	print "Waiting for a connection........."
	connection, client_addr = socket.accept()
	try:
		print "Connection recieved from ", client_addr
		while True:
            		data = connection.recv(50)
            		print >>sys.stderr, 'received "%s"' % data
            		if data:
                		print >> sys.stderr, 'sending data back to the client'
                		connection.sendall(data)
            		else:
                		print >>sys.stderr, 'no more data from', client_addr
                		break
	finally:
		connection.close()

