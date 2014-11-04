import socket
import dgramconn


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_addr = raw_input("Tell me the address of the server: ")
s_port = raw_input("Tell me the port of the server: ")

server = (s_addr,int(s_port))
sock.connect(server)

dc = dgramconn.DatagramConnection(sock)


message = raw_input()
dc.send(message)

data = dc.recv()
print data
