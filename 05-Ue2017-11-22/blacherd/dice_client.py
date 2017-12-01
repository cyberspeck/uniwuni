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


if len(sys.argv) != 2:
	print("Usage: {} zinkung(int)".format(sys.argv[0]))
	message = "help"
else:
	zinkung = string.atoi(sys.argv[1])
	message = "throw 1 {}".format(zinkung)



port = 56700
host = 'localhost'

s = connect(port, host)
s.send(message+"\r\n") #\r\n ist der Zeilenumbruch in Windows

# lesen der Antwort
data = s.recv(9192)
s.close()
print('Received:\n {}'.format(data))
