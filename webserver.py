import socket
import threading
import _thread
from hooks import eprint
import time

class webserver:
    def __init__(self, address, listen_backlog=1021, debug=True):
        self.debug = debug
        self.address = address
        self.listen_backlog = listen_backlog
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.debug == True:
            eprint('a new socket created')
        self.socket.bind(address)
        self.socket.listen(self.listen_backlog)
        if self.debug == True:
            eprint(f'started listening at ip: {address[0]}, port: {address[1]} accepting {self.listen_backlog} reqs as max.')
    
            
    def accept(self):
        conn, address = self.socket.accept()
        eprint(f'connected to {address[0]} : {address[1]}')
          
    def __del__(self):
        self.socket.close()