# for logging
from hooks import eprint

import time

# a class for handling webserver requests
class request_handler:
    def __init__(self, debug=True, bufferSize=1024, path='.'):
        # set variables
        self.debug = debug
        self.bufferSize = 1024
        self.path = path
    
    # you can create a thread of this function for each client
    # main request handler function
    def handle(self, conn, name=''):
        # start communicating
        while True:
            # wait for receiving new data
            data = conn.recv(self.bufferSize)
            # check if connection is going to end
            if not data:
                if self.debug == True:
                    eprint(name, ':', '__END__')
                # end the connection
                break
            # now the request is going to get handled

            self.default_answer(conn, data, name=name)

            if self.debug == True:
                eprint(name, ':', data)

    def default_answer(self, conn, data, name=''):
        header = bytes('HTTP/1.1 200 OK\n\n', 'utf-8')
        text = bytes('lol\n', 'utf-8')
        conn.send(header)
        for i in range(10):
            conn.send(text)
            time.sleep(1)

    # nothing yet.
    def __del__(self):
        pass