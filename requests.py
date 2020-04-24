import socket
from hooks import eprint

class request_handler:
    def __init__(self, debug):
        self.debug = debug
        self.bufferSize = 1024
    
    def handle(self, conn, name=''):
        while True:
            data = conn.recv(self.bufferSize)
            if not data:
                eprint(name, ':', '__END__')
                break
            eprint(name, ':', data)

    def __del__(self):
        pass