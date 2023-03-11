#!/bin/usr/python3

import sys

#het lijnnummer initialiseren buiten de for loop
line_num = 1

#bestanden overlopen die zijn doorgegeven
for file_path in sys.argv[1:]:

    #open bestand en print inhoud
    with open(file_path, 'r') as file:
        for line in file:
            print(f"{line_num:6}\t{line}", end="")
            line_num += 1