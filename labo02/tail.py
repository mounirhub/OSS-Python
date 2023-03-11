#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    file = open(file_path, 'r')
else:
    file = sys.stdin

#lijst om de laatste 10 regels bij te houden
last_lines = []

#leest het bestand en houd de laatste 10 regels bij
for line in file:
    #voegt element toe aan einde van lijst
    last_lines.append(line)
    if len(last_lines) > 10:
        #verwijdert element op plaats 0 (1ste element)
        last_lines.pop(0)

for line in last_lines:
    print(line, end='')