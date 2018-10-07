import socket
import sys

#Create Socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 1000)
socket.connect(addr)

try:
    # Send a message
    message = 'Hello Serve, This is Client'
    socket.sendall(message)

    # Look for response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = socket.recv(50)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'Closing socket'
    socket.close()
