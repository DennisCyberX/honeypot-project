import unittest
import socket
import threading
import time
from scripts.honeypot import start_honeypot

class TestHoneypot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the honeypot in a separate thread
        cls.honeypot_thread = threading.Thread(target=start_honeypot)
        cls.honeypot_thread.daemon = True
        cls.honeypot_thread.start()
        time.sleep(1)  # Wait for the honeypot to start

    def test_connection(self):
        # Test connecting to the honeypot
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 2222))
        response = client.recv(1024)
        self.assertIn(b"Welcome", response)
        client.close()

if __name__ == "__main__":
    unittest.main()
