import socket
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='logs/honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Honeypot configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 2222       # Port to listen on (non-standard port to avoid conflicts)

def handle_connection(client_socket, address):
    """Handle incoming connections and log activity."""
    logging.info(f"Connection from {address}")
    client_socket.send(b"Welcome to the honeypot!\n")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        logging.info(f"Data received from {address}: {data.decode('utf-8', errors='ignore')}")
        client_socket.send(b"Command not recognized.\n")
    client_socket.close()

def start_honeypot():
    """Start the honeypot server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    logging.info(f"Honeypot started on {HOST}:{PORT}")
    print(f"Honeypot running on {HOST}:{PORT}...")

    while True:
        client_socket, address = server.accept()
        handle_connection(client_socket, address)

if __name__ == "__main__":
    start_honeypot()
