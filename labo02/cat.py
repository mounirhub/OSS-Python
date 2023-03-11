#!/usr/bin/python3

import sys

#haalt bestand om dat is opgegeven
#argv[1] = kiest 2de argument dus slaat naam van script zelf over
file_path = sys.argv[1]

#Open en print
with open(file_path, 'r') as file:
    contents = file.read()
    print(contents)