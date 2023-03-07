#!/usr/bin/python3

ff = open('newfile', 'w')

print('type "ff" is:', type(ff))

print('properties en methods of ff:', dir(ff))

print('ff.closed:', ff.closed)
print('ff.close', ff.close)

ff.close()
print('ff.closed:', ff.closed)