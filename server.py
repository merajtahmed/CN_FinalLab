import socket

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind IP and port
server_socket.bind(("localhost", 8082))


# listen for client
server_socket.listen(1)
print("Server is waiting for connection...")

# accept client
conn, addr = server_socket.accept()
print("Connected with:", addr)

# receive data
data = conn.recv(1024).decode()
print("Client says:", data)

# send reply
conn.send("Hello from server".encode())

# close connection
conn.close()
