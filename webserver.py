import socket
import threading
from hooks import eprint
import time
from requests import request_handler

class webserver:
    def __init__(self, address, listen_backlog=1021, debug=True, bufferSize=1024):
        self.debug = debug
        self.address = address
        self.bufferSize = bufferSize
        self.listen_backlog = listen_backlog
        self.threads = list()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.debug == True:
            eprint('a new socket created')
        self.socket.bind(address)
        self.socket.listen(self.listen_backlog)
        if self.debug == True:
            eprint(f'started listening at ip: {address[0]}, port: {address[1]} accepting {self.listen_backlog} reqs as max')
        self.handler = request_handler(self.debug)

    def req_handler(self, conn):
        while True:
            data = conn.recv(self.bufferSize)
            if not data:
                eprint('end')
                break
            eprint(data)

    def start_receiving(self):
        while True:
            self.accept()

    def accept(self):
        conn, address = self.socket.accept()
        if self.debug == True:
            eprint(f'connected to {address[0]} : {address[1]}')
            self.handler.bufferSize += 1
        threading.Thread(target=self.handler.handle, args=(conn,), kwargs={'name':address}).start()

          
    def __del__(self):
        self.socket.close()
