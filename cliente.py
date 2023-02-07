import socket

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtém o endereço IP e a porta do servidor
host = socket.gethostname()
port = 12345

# Liga o socket do cliente ao endereço IP e porta do servidor
client_socket.connect((host, port))
print("enviado")

# Envia uma string para o servidor
string_to_send = "Hello, server!"
client_socket.send(string_to_send.encode('utf-8'))

# Fecha o socket do cliente
client_socket.close()
