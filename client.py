import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((socket.gethostname(), 1234))

message = my_socket.recv(1024)
print(message.decode("utf-8"))