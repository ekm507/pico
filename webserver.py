# we use this builtin library for socket programming
import socket
# for handling multiple requests at time
import threading
# better print function
from hooks import eprint
# main request handler function
from requests import request_handler

# webserver object
class webserver:
    # address: address to listen to
    # listen backlog: maximum number of clients at once
    # debug: logging
    # bufferSize: data receiving buffer size
    def __init__(self, address, listen_backlog=1021, debug=True, bufferSize=1024, path='./content'):
        # set vars
        self.debug = debug
        self.address = address
        self.bufferSize = bufferSize
        self.listen_backlog = listen_backlog
        self.path = path
        # define a new socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.debug == True:
            eprint('a new socket created')
        # bind socket to the address
        self.socket.bind(address)
        # start listening
        self.socket.listen(self.listen_backlog)
        if self.debug == True:
            eprint(f'started listening at ip: {address[0]}, port: {address[1]} accepting {self.listen_backlog} reqs as max')
        # define a new request handler object for later uses
        self.handler = request_handler(self.debug, bufferSize=self.bufferSize, path=self.path)

    # staru accepting clients
    def start_receiving(self):
        # just a loo for accept function
        while True:
            self.accept()

    # accept a client and make a connection
    def accept(self):
        # wait for a new connection
        conn, address = self.socket.accept()
        if self.debug == True:
            eprint(f'connected to {address[0]} : {address[1]}')
        # with new connection, start a new thread of request handler
        threading.Thread(target=self.handler.handle, args=(conn,), kwargs={'name':address}).start()

    def __del__(self):
        # close the socket when object is getting deleted
        self.socket.close()
