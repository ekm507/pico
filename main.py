from webserver import webserver
import sys

def main():
    try:
        HOST = '0.0.0.0'
        PORT = 1234
        address = (HOST, PORT)
        ws = webserver(address, debug=True)
        ws.start_receiving()
    except KeyboardInterrupt:
        del ws
        sys.exit(" Keyboard Interrupt Exit(ctrl+c)")
        


if __name__ == "__main__":
    main()
