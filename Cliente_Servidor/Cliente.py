import socket
ip = 'localhost'
port = 8002
addr = ((ip, port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
mensagem = ' '

while(mensagem != 'sair'):
   mensagem = input('Digite uma mensagem para ser enviada  ao servidor: ')
   try:
      client_socket.send(mensagem.encode())
      # print('Mensagem enviada !')
      print('Mensagem recebida: '+ client_socket.recv(1024).decode())
   except:
      print('A mensagem não foi enviada !')

client_socket.close()