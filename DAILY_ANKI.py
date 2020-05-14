# imports

# list
from functools import partial
from pathlib import Path
from functools import wraps
import math
import traceback
import re
import itertools
from contextlib import contextmanager
import os
fruits = ['apples', 'bananas', 'oranges', 'potatoes']

os.chdir('/Users/ilja/Dropbox/ATBS')

# dict
doggo = {
    "name": 'haisch',
    "surname": 'tilevich',
    'job': 'doge',
    'age': 10,
    'abilities': ['bark', 'poop', 'party']
}


# class
class Person(object):

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def implicit(self):
        print('i am implicit!')

    def overriden(self):
        print('not yet over-riden!')

    def altered(self):
        print('to be altered!')


ilja = Person('ilja', 'moi', 27)

##############################################################################

# """
# linear search - n
# binary search - nlogn or logn depending on whether L[:] is used
# bogus sort
# selection sort / bubble sort = n**2
# merge sort - nlogn
# """
#
# ##############################################################################


def multiply(x, y, z):
    return x*y+z


double = partial(multiply, 2)
triple = partial(double, 5)
print(triple(1))
