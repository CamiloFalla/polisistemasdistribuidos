import socket

def main():
    server_host = "localhost"
    server_port = 5555

    # Conectar al servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Solicitar el número de teléfono al usuario
    phone_number = input("Ingrese el número de teléfono: ")

    # Enviar el número de teléfono al servidor
    client_socket.send(phone_number.encode())

    # Recibir y mostrar la respuesta del servidor
    response = client_socket.recv(1024).decode()
    print("Respuesta del servidor:", response)

    client_socket.close()

if __name__ == "__main__":
    main()
