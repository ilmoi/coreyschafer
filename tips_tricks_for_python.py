# 1 - quick way to write conditoins

from getpass import getpass
condition = True

"""
instead of writing
if condition:
    x = 1
else:
    x = 0
"""

x = 1 if condition else 0
print(x)

# 2 - you can separate numbers out using underscores, without affecting them!
num1 = 1_000_000_000
print(num1)
# to format the output:
print(f'{num1:,}')

# 4

names = ['spiderman', 'ironman', 'iljaman']
for index, name in enumerate(names):
    hero = names[index]
    print(f'the {index} hero is {hero}')

heros = ['spiderman', 'superman', 'batman']
names = ['peter parker', 'clark kent', 'bruce wayne']
universes = ['marvel', 'dc', 'marvel']

for hero, name, universe in zip(heros, names, universes):
    print(f'{hero} is actually {name} from {universe}')

for value in zip(heros, names, universes):
    print(value)

# 5 unpacking
a, b, *c = (1, 2, 3, 4, 5)
print(a, b, c)

a, b, *c, d = [1, 2, 3, 4, 5, 6]
print(a, b, c, d)

# 6 you can dynamically add values to a call


class Person(object):
    pass


person = Person()

setattr(Person, 'key', 'value')
first = getattr(Person, 'key')

print(person.key)
print(first)

attrs = {'name': 'ilja', 'last': 'mois'}
for key, value in attrs.items():
    setattr(person, key, value)

for key in attrs.keys():
    print(getattr(person, key))

# 7 securely accept passwords

# username = input('username: ')  # not secure
# password = getpass('password: ')  # this will hide it in termianl
#
# print('logging in ')

# https://www.youtube.com/watch?v=zdJEYhA2AZQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=108

# dont ever pass en empty list as an argument to a function


def func(name, our_list=[]):
    our_list.append(name)
    print(our_list)


LL = ['ilja']
func('vadim', LL)  # all good = ilja, vadim

# but now watch this
func('vadim')  # vadim
func('aaron')  # vadim, aaron
func('potato')  # vadim, aaron, potato
# instead of creating a new list each time, it appends


def func(name, our_list=None):
    if our_list == None:
        our_list = []
    our_list.append(name)
    print(our_list)


func('vadim')  # vadim
func('aaron')  # aaron
func('potato')  # potato
# good!
