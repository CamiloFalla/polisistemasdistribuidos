# test_simple_server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5555))
server_socket.listen()

print("Servidor escuchando en 0.0.0.0:5555...")
server_socket.accept()  # Mantener el servidor escuchando

