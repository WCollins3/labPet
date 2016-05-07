import socket
import sys
import argparse
import threading

message_delim = "$%$"

# IMPORTANT INFO WHEN RUNNING: Must run the following line
# python3 pet_server.py <ip address> <port>
# FOR EXAMPLE:
# python3 pet_server.py localhost 8080

def handle_client(client_socket: socket.socket):
    client_socket.send(("Connected" + message_delim).encode())

    connect_message = ""
    while connect_message.endswith(message_delim) == False:
        connect_message += client_socket.recv(1024).decode()
    print("Successfully connected to the pet client!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('listen_address')
    parser.add_argument('port_number')

    args = parser.parse_args()

    listen_address = args.listen_address

    try:
        port_number = int(args.port_number)
    except ValueError:
        sys.exit('Port number must be an integer')

    max_port_number = 65535

    if port_number > max_port_number or port_number < 0:
        sys.exit('Port number out of range')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((listen_address, port_number))
    server_socket.listen(5)
    print('listening on {0}:{1}'.format(listen_address, port_number))

    try:
        while True:
            client_socket, address = server_socket.accept()
            thread = threading.Thread(target=handle_client,
                                      args=(client_socket,),
                                      daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print('Main caught keyboard interrupt')


if __name__ == '__main__':
    main()