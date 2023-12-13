import ssl 
import socket

client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server_ip = '127.0.0.1'
server_port = 443

client_socket.connect((server_ip , server_port))
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

ssl_client_socket = context.wrap_socket(client_socket , server_hostname=server_ip)


try:
    ssl_client_socket.send(b'HEELO , server !' )
    response = ssl_client_socket.recv(1024)
    print("server respose" , response.decode())

except ssl.SSLError as e:
    print(e)
finally :
    ssl_client_socket.close()
