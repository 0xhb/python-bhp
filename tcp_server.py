import socket
import threading

IP = "0.0.0.0"
port = 9999


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, port))
    server.listen(5)
    print(f"[*] Listening on {IP}:{port}")

    def handle_client(client_socket):
        with client_socket as sock:
            request = sock.recv(4096)
            print(f"[*] Received: {request.decode()}")
            sock.send(b"ACK")

    while True:
        client, address = server.accept()
        print(f"[*] Accepting request from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == '__main__':
    main()
