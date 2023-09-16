import socket

HOST = 'localhost'  # Endereço do servidor
PORT = 12345        # Porta do servidor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Digite uma mensagem: ")
    client_socket.send(message.encode('utf-8'))

    #receber mensagem do servidor
    server_message = client_socket.recv(1024).decode('utf-8')
    print(f"Servidor diz: {server_message}")
