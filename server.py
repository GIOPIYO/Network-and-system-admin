import socket
#firewall rules
def handle_connection(client_socket):
    
    allowed_ips = ['127.0.0.1'] 

    client_address = client_socket.getpeername()[0]
    if client_address not in allowed_ips:
        print(f"Connection from {client_address} rejected (firewall rule)")
        return

    print('Got connection from', client_address)

    message = 'Thank you for connecting'
    client_socket.send(message.encode())
    client_socket.close()
#server code
def main():
    s = socket.socket()
    port = 3456

    try:
        s.bind(('', port))
        print(f'Socket binded to port {port}')
    except socket.error as e:
        print(str(e))
        return

    s.listen(5)
    print('Socket is listening')

    while True:
        try:
            c, addr = s.accept()
            handle_connection(c)
        except socket.error as e:
            print(str(e))
            break

    s.close()
#run main
if __name__ == "__main__":
    main()
