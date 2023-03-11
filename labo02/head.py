#!/usr/bin/python3

import sys

#open het bestand  
file_path = sys.argv[1]
file = open(file_path, 'r')

#druk eerste 10 regels
for i in range(10):
    line = file.readline()
    if not line:
        break
    print(line, end='')