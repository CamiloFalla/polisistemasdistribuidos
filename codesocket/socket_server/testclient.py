import socket

def main():
    server_host = 'localhost'  # Usar la dirección IP del servidor si está en una máquina diferente
    server_port = 5555

    # Crear un socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        client_socket.connect((server_host, server_port))
        print(f"Conectado a {server_host} en el puerto {server_port}")

        # Enviar un mensaje simple
        message = "Hola servidor, desde el cliente!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Mensaje enviado: {message}")

        # Opcional: Recibir una respuesta del servidor y cerrar
        # response = client_socket.recv(1024)
        # print(f"Respuesta recibida: {response.decode('utf-8')}")

    finally:
        # Cerrar la conexión
        client_socket.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()
