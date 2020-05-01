# webserver
from webserver import webserver
# basic system functions
import sys
import os

# main function
def main():
    # this is for closing socket when errors occur
    try:
        # set listening host and port
        HOST = '0.0.0.0'
        # try getting port number from shell
        if len(sys.argv) > 1:
            PORT = int(sys.argv[1])
        # if not provided by shell, default port number is this
        else:
            PORT = 1234
        # set listening address tuple
        address = (HOST, PORT)
        # create a new webserver object. with log mode set as true
        ws = webserver(address, debug=True)
        # let webserver handle its requests
        ws.start_receiving()
    # when ctrl+C pressed:
    except KeyboardInterrupt:
        # delete webserver object close the socket.
        del ws
        # exit the program
        sys.exit(" Keyboard Interrupt Exit(ctrl+c)")
        

# start the program
if __name__ == "__main__":
    main()
