import sys
import socket
import argparse

# IMPORTANT INFO WHEN RUNNING: Must run the following line
# python3 pet_client.py <server ip address> <server port>
# Must run after server is already running
# FOR EXAMPLE: if server is running on localhost 8080, enter the following line
# python3 pet_server.py localhost 8080

message_delim = "$%$"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('server_address')
    parser.add_argument('port_number')

    args = parser.parse_args()

    server_address = args.server_address

    try:
        port_number = int(args.port_number)
    except ValueError:
        sys.exit('Port number must be an integer')

    max_port_number = 65535

    if port_number > max_port_number or port_number < 0:
        sys.exit('Port number out of range')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((server_address, port_number))

    connect_message = ""
    while connect_message.endswith(message_delim) == False:
        connect_message += server_socket.recv(1024).decode()
    print("Connection from pet server received!")

    server_socket.send(connect_message.encode())

if __name__ == '__main__':
    main()
