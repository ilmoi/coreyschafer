# ITERATOR = object with a state so that it remmebers where it is during iteration
# to be an iteratOR it must have the __next__() method
# eg a list is NOT an iterator
nums = [1, 2, 3]
dir_nums = dir(nums)
if '__next__' in dir_nums:
    print('NUMS has a NEXT method')

# however, list is ITERABLE.
# to be iteraBLE it must have __iter__() method
if '__iter__' in dir_nums:
    print('NUMS has an ITER method')

# another charcaterist of an iteraBLE is that you can use it in a for loop:
for num in nums:
    print(f'for looping through this bad boy time {num}')

# we can convert an iteraBLE into an interatOR
i_nums = nums.__iter__()
# or alternatively (and more beautifully, as we should not call dunders directly) we could have called
# i_nums = iter(nums)

print(i_nums)
dir_inums = dir(i_nums)
if '__next__' in dir_inums:
    print('I_NUMS has a NEXT method')
# success

# lets print out next values
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# the next one would produce an exception

# we can do it more elegantly
while True:
    try:
        print(next(i_nums))
    except StopIteration:
        print('breaking out')
        break

# lets create our own object that is going to be both iteraBLE and iteratOR


class MyRange(object):

    def __init__(self, start, end):
        self.value = start
        self.end = end

    # this must return an iteratOR object. Now what is an iteratOR object? Well that's just an object that has __next__
    # if we're planning to add __next__ to this class then we just return itself!
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


myrange = MyRange(1, 10)
print(myrange)
# it's an object

# for i in myrange:
#     print(i)
# it works, so we know it's an iteraBLE

print('-'*50)
print(next(myrange))
print(next(myrange))
print(next(myrange))
# this works too, means it's an iteratOR


# we can use a generator function, which also has an __iter__ and a __next__ method
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


my_r = my_range(1, 10)

print('-'*50)
print(next(my_r))
print(next(my_r))
print(next(my_r))

# so generators are useful when you're dealing with super long lists that you don't want to store in memory in full
# imagine writing a password cracker, for example

# RECAP
# iteraBLE = can be looped over, has an __iter__() method that returns an iteratOR object
# iteratOR = must have a state and define a __next__ method that acesses elements inside of the container one a a time

nums = [1, 2, 3, 4]
letts = ['a', 'b', 'c', 'd']
L = [str(n)+str(l) for n, l in zip(nums, letts)]
print(L)
