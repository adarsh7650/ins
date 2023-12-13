import socket
import ssl 

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0' , 443))
server_socket.listen()

certfile ='localhost.crt'
keyfile = 'localhost.key'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)

print ( "Server is lsitening on port 443")

while True :
    client_socket , client_address = server_socket.accept()
    ssl_client_socket = context.wrap_socket(client_socket , server_side=True)
    try :
        data = ssl_client_socket.recv(1024)
        print("recevied :  ", data.decode())
        ssl_client_socket.send(b"helllo world")
        
    except ssl.SSLError as e:
        print ( "SSl ERROR is ", e)
    finally :
        ssl_client_socket.close()