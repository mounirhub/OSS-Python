#!/usr/bin/python3

import sys

# initial counts
num_lines = 0
num_words = 0
num_chars = 0

# file provided as argument
filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        #telt lijnen
        num_lines += 1
        #telt woorden
        words = line.split()
        num_words += len(words)
        #telt karakters
        num_chars += len(line)

print(f"Aantal lijnen: {num_lines}, Aantal woorden: {num_words}, Aantal karakters: {num_chars}")