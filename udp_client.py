import socket

host = "www.google.com"
port = 80

print("step 1")
# make a socket object over udp
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("step 1")
# send some data to the server
client.sendto(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n", (host, port))

print("step 1")
# recieve server response
data, addr = client.recvfrom(4096)

print("step 1")
print(data.decode())
client.close()
