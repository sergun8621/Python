from socket import socket, AF_INET, SOCK_DGRAM
srv_addr = "192.168.10.10"
srv_port = 41000
addr = (srv_addr, srv_port)
sock = socket(AF_INET, SOCK_DGRAM)
n = sock.sendto(b"HELLO_UDP!\n", addr)
print(sock.recvfrom(n))


