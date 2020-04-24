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
    
    # you can create a thread of this function for each client
    # main request handler function
    def handle(self, conn:socket.socket, name=''):
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
                eprint(name, ': request is:\n', str(data, encoding='utf-8'))
            
            conn.shutdown(1)

        conn.close()
            

    def default_answer(self, conn, data, name=''):
        text = str(data, 'utf-8')
        method = text.split(' ')[0]
        link = text.split(' ')[1]
        host = text.split('\n')[1]
        if method == 'GET':
            if link == '/':
                filename = self.path + '/index.html'
            elif link == '/word':
                cmd = ['python', f'{self.path}/back/words.py', '6', 'time']
                subprocess.Popen(cmd).wait()
                filename = self.path + '/back/words-out.html'
                header = 'HTTP/1.0 200 OK\nContent-Type: text/html; charset=utf-8\nLanguage: fa\n\n'.encode('utf-8')
                content = open(filename, 'rb').read()
                print(content)
            else:
                filename = self.path + link.split('?')[0]
                print(filename)
            try:
                header = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n'.encode('utf-8')
                content = open(filename, 'rb').read()
            except FileNotFoundError:
                header = 'HTTP/1.0 404 Not Found\n\n'.encode('utf-8')
                content = open(self.path+'/errors/404.html').read().encode('utf-8')
            texttosend = header + content
            conn.send(texttosend)

    # nothing yet.
    def __del__(self):
        pass