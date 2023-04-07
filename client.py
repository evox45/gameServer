import socket
import threading

# Echo Function
def echo(c: socket.socket):
    # Receive data from the client
    data = c.recv(1024).decode('utf-8')

    print("from connected user: " + str(data))

    # Upper case the message sent from the client
    data = str(data).upper()

    print("sending: " + str(data))

    # Send the uppercase data back to the client
    c.send(data.encode('utf-8'))

    # Close the connection
    c.close()

# Main Server
def main():
    print("Starting server...")

    # Host and Port to start the server on
    host = '127.0.0.1'
    port = 4040

    # Create a socket object
    s = socket.socket()

    # Bind to the host and port
    s.bind((host,port))

    # Start listening for connections
    s.listen(1)

    while True:
        # Accept a connection, is a blocking function
        c, addr = s.accept()

        # Print the address of the connection
        print("Connection from: " + str(addr))

        # Create a new thread to handle the connection
        t = threading.Thread(target=echo, args=([c]))
        t.start()
    
    s.close()

if __name__ == '__main__':
    main()