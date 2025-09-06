import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))
server_socket.listen()
print("Server is listening on port 65432...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024).decode()
print(f"Client says: {data}")

conn.send("Hello from Server!".encode())

conn.close()
server_socket.close()