import socket
host = 'localhost'
port = 8002
addr = ((host, port))
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print('aguardando conexao...')
con, cliente = serv_socket.accept()
print('conectado!')
print('aguardando mensagem...')

mensagem = ' '
while(mensagem != 'sair'):
    recebe = con.recv(1024)
    print('mensagem recebida: ' + recebe.decode())
    mensagem = input('Digite uma mensagem para enviar ao cliente: ')
    con.send(mensagem.encode())

serv_socket.close()

