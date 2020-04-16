# do not delete

# list
from contextlib import contextmanager
import os
fruits = ['apples', 'bananas', 'oranges', 'potatoes']


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

    def __lt__(self, other):
        if self.age <= other.age:
            return True
        else:
            return False

    def implicit(self):
        print(f'this is an implicit call by {self.first}')

    def overriden(self):
        print(f'this is an overridden call by {self.first}')

    def altered(self):
        print(f'this is an alterd call by {self.first}')


ilja = Person('ilja', 'moi', 27)
vadim = Person('vadim', 'mole', 30)

##############################################################################

"""
docstring
from __future__ import
__all__, __version__, __author__ = []
import os


"""

##############################################################################

a = hex(ord("б"))
print(a)

print("б" == '\u0431' == '\U00000431')

b = "б".encode('utf-8')
print(b)
