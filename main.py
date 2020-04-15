import socket
import os

HOST = '0.0.0.0'
PORT = 80
PATH = os.getcwd() + '/content'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Started listening on port {PORT}')
    while(True):
        conn, address = s.accept()
        with conn:
            print('connected by', address)
            try:
                data = conn.recv(1024)
            except:
                print('error conn.recv()')
                continue
            if not data:
                break
            text = str(data, 'utf-8')
            print(f'request is:\n {text}')
            method = text.split(' ')[0]
            link = text.split(' ')[1]
            if method == 'GET':
                if link == '/':
                    filename = PATH + '/index.html'
                else:
                    filename = PATH + link.split('?')[0]
                print(filename)
                try:
                    header = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n'.encode('utf-8')
                    content = open(filename).read().encode('utf-8')
                except FileNotFoundError:
                    header = 'HTTP/1.0 404 Not Found\n\n'.encode('utf-8')
                    content = open(PATH+'/errors/404.html').read().encode('utf-8')
                texttosend = header + content
                conn.send(texttosend)