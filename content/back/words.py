import csv
import random
from sys import argv
import time
import os

PATH = os.getcwd() + '/content/back'

print(argv)

# number of words to get
if len(argv) > 1:
    wordsIwant = int(argv[1])
else:
    wordsIwant = 6

# set the random seed
if len(argv) > 2:
    if argv[2].isnumeric():
        random.seed(int(argv[2]))
    elif argv[2] == 'time':
        random.seed(time.time())
else:
    random.seed(0)

# a line worth of a few things
words_list = list(w[1] for w in csv.reader(open(f'{PATH}/persian-words.csv')))

a = []
for i in range(wordsIwant):
    a.append(random.choice(words_list))
with open(f'{PATH}/words-out.html', 'w') as outfile:
    header = '<html lang="fa">\n<head>\n<meta charset="UTF-8">\n</head>'
    footer = '</html>'
    print(header, file=outfile)
    for w in a:
        print('<p>', file=outfile)
        print(w, file=outfile)
    print(footer, file=outfile)
    print(a)
