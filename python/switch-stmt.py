#!/usr/bin/env python
# How to simulate a switch statement in Python

size_to_point = {'small':7, 'normal':9, 'large':12,0:9}
size = 'small'
point_size = size_to_point.get(size,size)
print("Point size from {} is {}".format(size, point_size))

# From Python 3.10, the case statement can be used instead

"""
match size:
    case 'small': pt_size = 7
    case 'normal': pt_size = 9
    case 'large': pt_size = 12

print("Using a match statement, point size from {} is {}".format(size, pt_size))

"""