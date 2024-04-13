import socket
import psycopg2
import threading
from psycopg2 import Error

# Configuración de la conexión a la base de datos
DB_HOST = "localhost"
DB_PORT = "5435"
DB_NAME = "ubicaciones_db"
DB_USER = "user"
DB_PASSWORD = "sistdist"

def connect_to_database():
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        return connection
    except Error as e:
        print(f"Error while connecting to PostgreSQL: {e}")
        return None

def handle_client_connection(client_socket, db_connection):
    try:
        while True:
            # Recibir el número de teléfono del cliente
            phone_number = client_socket.recv(1024).decode()
            if not phone_number:
                break

            # Buscar la información en la base de datos
            with db_connection.cursor() as cursor:
                cursor.execute("SELECT dir_nombre FROM personas WHERE dir_tel = %s", (phone_number,))
                person = cursor.fetchone()

                if person:
                    response = f"Nombre: {person[0]}"
                else:
                    response = "Persona no encontrada"

                client_socket.send(response.encode())
    finally:
        client_socket.close()

def client_thread(client_socket, db_connection):
    handle_client_connection(client_socket, db_connection)

def main():
    # Configurar el servidor
    server_host = "0.0.0.0"
    server_port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print("Server listening on port", server_port)

    # Conectar a la base de datos
    db_connection = connect_to_database()

    if db_connection:
        try:
            while True:
                client_socket, _ = server_socket.accept()
                print("Client connected")
                # Crear un nuevo hilo para manejar la conexión del cliente
                thread = threading.Thread(target=client_thread, args=(client_socket, db_connection))
                thread.start()
        finally:
            db_connection.close()
            server_socket.close()

if __name__ == "__main__":
    main()
