import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 4040))

server_socket.listen(5)

time.sleep(10)