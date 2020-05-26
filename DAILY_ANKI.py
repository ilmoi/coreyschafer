from collections import namedtuple
import itertools
import random
import json
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

    def __repr__(self):
        return f'{self.__class__.__name__}({self.first}, {self.last}, {self.age})'


ilja = Person('ilja', 'moi', 27)

##############################################################################

"""
kubectl label pod POD_NAME key=value
kubectl get pod -l key=value
"""
#
# ##############################################################################
