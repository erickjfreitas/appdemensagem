import socket

HOST = 'localhost'  # Endereço do servidor
PORT = 12345        # Porta do servidor

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor de bate-papo ouvindo em {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Cliente diz: {message}")

        #respondendo a mensagem
        response = input("Digite uma resposta para o cliente: ")
        client_socket.send(response.encode('utf-8'))
