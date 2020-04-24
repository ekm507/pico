# for logging
from hooks import eprint

# a class for handling webserver requests
class request_handler:
    def __init__(self, debug=True, bufferSize=1024):
        # set variables
        self.debug = debug
        self.bufferSize = 1024
    
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
            if self.debug == True:
                eprint(name, ':', data)

    # nothing yet.
    def __del__(self):
        pass