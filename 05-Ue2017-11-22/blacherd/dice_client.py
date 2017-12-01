# -*- coding: utf-8 -*-
import socket, sys, string

def connect(port, host):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except(socket.error, msg):
		s = None
	try:
		s.connect((host,port)) # Verbinden
	except(socket.error, msg):
		s.close()
		s = None
	if s is None:
		print('Can not open socket {}'.format(msg))
		sys.exit(1)
	return s


port = 56700
host = 'localhost'

if len(sys.argv) != 3:
	print("Usage: {} würfe(int) zinkung(int)".format(sys.argv[0]))
	message = "help"
else:
	zinkung = string.atoi(sys.argv[2])
	N = string.atoi(sys.argv[1])
	message = "throw {} {}".format(N, zinkung)

s = connect(port, host)
s.send(message+"\r\n") #\r\n ist der Zeilenumbruch in Windows

# lesen der Antwort
data = s.recv(9192)
s.close()
print('Received:\n {}'.format(data))

if message == "help": sys.exit(0);

data = data.strip()
throws = []

for d in data:
    throws.append(int(d))

# throw enthält alle Würfe als Liste
