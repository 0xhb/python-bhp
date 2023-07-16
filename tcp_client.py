import socket

host = "www.google.com"
port = 80

print("step 1")
# making the socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("step 2")
# establish the connection with the target
client.connect((host, port))
print("step 3")
# send some data to the server
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
print("step 4")
# receive some data
response = client.recv(4096)

print("step 5")
print(response.decode())
client.close()
