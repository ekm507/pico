# for logging
from hooks import eprint
import subprocess
import time
import socket

# a class for handling webserver requests
class request_handler:
    def __init__(self, debug=True, bufferSize=1024, path='./content'):
        # set variables
        self.debug = debug
        self.bufferSize = 1024
        self.path = path

        self.backs = list()
        backs = open('backs.conf', 'r').read()
        for line in backs.split('\n'):
            if line[0] == '#':
                pass
            else:
                link = line.split(' ')[0]
                outfilename = line.split(' ')[1]
                runnable = line[len(link) + len(outfilename) + 2 :]
                self.backs.append((link, outfilename, runnable))
        
    
    # you can create a thread of this function for each client
    # main request handler function
    def handle(self, conn:socket.socket, name=''):
        # start communicating
        try:
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
                    eprint(name, ': request is:\n', str(data, encoding='utf-8'))
                
                conn.shutdown(1)
            conn.close()
        except KeyboardInterrupt:
            conn.close()
            

    def default_answer(self, conn, data, name=''):
        text = str(data, 'utf-8')
        method = text.split(' ')[0]
        link = text.split(' ')[1]
        name = link.split('?')[0]
        params = link.split('?')[1:]
        host = text.split('\n')[1]
        data = b''
        if method == 'GET':
            status = 0
            for a, b, c in self.backs:
                if name == a:
                    cmd = c.split(' ') + params
                    print(cmd)
                    subprocess.Popen(cmd).wait()
                    f = open(self.path + b, 'r')
                    data = f.read().encode('utf-8')
                    f.close()
                    status = 200
            if status == 0:
                if name == '/':
                    filename = self.path + '/index.html'
                    status = 200
                else:
                    filename = self.path + link.split('?')[0]
                    status = 200
                try:
                    data = open(filename, 'rb').read()
                    status = 200
                except FileNotFoundError:
                    status = 404
           
            if status == 200:
                header = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n'.encode('utf-8')
            elif status == 404:
                header = 'HTTP/1.0 404 Not Found\n\n'.encode('utf-8')
                data = open(self.path + '/errors/404.html', 'rb').read()
            else:
                pass
            texttosend = header + data
            conn.send(texttosend)

    # nothing yet.
    def __del__(self):
        pass