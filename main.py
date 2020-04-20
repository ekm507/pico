import socket
import threading
import _thread
from hooks import eprint
import time


def parse_request(data:bytes):
    time.sleep(1)
    eprint(data)

def req_handler(conn:socket.socket):
    while True:
        data = conn.recv(1024)
        if not data:
            eprint('END')
            break
        
        parse_request(data)

    conn.close()

def main():
    HOST = '0.0.0.0'
    PORT = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.listen(100)
    eprint(f'started listening on port {PORT}')

    while True:
        conn, address = s.accept()

        eprint(f'connected to {address[0]} : {address[1]}')

        _thread.start_new_thread(req_handler, (conn,))

    s.close()

if __name__ == "__main__":
    main()
.