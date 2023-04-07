import socket

# Main Client
def main():

    # Host and Port to connect top
    print("Connecting to server...")
    host = '127.0.0.1'
    port = 4040

    # Create a socket object
    s = socket.socket()

    # Connect to the server
    s.connect((host,port))

    # Send a message to the server
    message = input("-> ")
    s.send(message.encode('utf-8'))

    # Receive data from the server
    data = s.recv(1024).decode('utf-8')
    print ("Received from server: " + data)

    # Close the connection
    s.close()

if __name__ == '__main__':
    main()