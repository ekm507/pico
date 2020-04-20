import sys
import time

def eprint(value):
    if value is None:
        return
    text = repr(value)
    sys.stdout.write('\u001b[36m')
    sys.stdout.write('* ')
    sys.stdout.write('\u001b[0m')
    sys.stdout.write((time.ctime(time.time())))
    sys.stdout.write('\u001b[31;1m')
    sys.stdout.write(' - ')
    sys.stdout.write('\u001b[0m')
    try:
        sys.stdout.write(text)
    except:
        sys.stdout.write('error')
    sys.stdout.write('\n')
