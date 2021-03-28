import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind( (socket.gethostname(), 1234) )
my_socket.listen(5)

while True:
    conection, address = my_socket.accept()
    print(f"Nueva conexion establecida: {address}")
    conection.send(bytes("Hola, te saludo desde el servidor", "utf-8"))
    conection.close()