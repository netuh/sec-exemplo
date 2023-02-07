import socket

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtém o endereço IP e a porta do servidor
host = socket.gethostname()
port = 12345

# Liga o socket do servidor ao endereço IP e porta especificados
server_socket.bind((host, port))
print("Bind")

# Inicia o processo de escuta
server_socket.listen(5000)
print("Recebendo")

# Aceita a conexão de um cliente
client_socket, client_address = server_socket.accept()
print("Recebido")

# Recebe a string enviada pelo cliente
received_string = client_socket.recv(1024).decode('utf-8')

# Imprime a string recebida
print("String recebida do cliente:", received_string)

# Fecha o socket do cliente
client_socket.close()

# Fecha o socket do servidor
server_socket.close()
