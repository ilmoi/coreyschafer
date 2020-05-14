import functools
import random
import itertools
import operator
import os

os.chdir('/Users/ilja/Dropbox/corey')


# ==============================================================================
# THIS FIRST PART IS FROM COREY
# https://www.youtube.com/watch?v=Qu3dThVy6KQ

print("-------------------- COUNT --------------------")
# we can basically create an arbitrary iteraTOR (has a __next__ method)
counter = itertools.count(start=5, step=5)

# this would go into an infinite loop
# for num in counter:
#     print(num)

# we can get one item at a time
print(next(counter))
print(next(counter))
print(next(counter))

# why is this useful?
# for once it saves us from having to write generators, eg for even numbers


def even_gen():
    n = 0
    while True:
        yield n
        n += 2


# the reason we need to assign even_gen to a variable before passing it into the list is because otherwise it creates a NEW GENERATOR on every iteration, and so next always gets the next value of 0.
evens_ = even_gen()
evens = list(next(evens_) for _ in range(5))
print(evens)

# accepts non integer values too
weirdos = itertools.count(start=0.5, step=0.73)
print(list(next(weirdos) for _ in range(5)))

# accepts negative values
negos = itertools.count(start=-1, step=-234)
print(list(next(negos) for _ in range(5)))

# BUT - the real power of the above count function is that it produces an INFINITE series!
# why do we care about an infinite series? we care about it if we want to pair with a list of variable length, like the below
counter = itertools.count()
nums = [100, 200, 300, 400]
daily_data = list(zip(nums, counter))
print(daily_data)
# in doing this we emulated the enumerate() function, except WE NEVER USED A FOR LOOP!


# note that zip works until the SHORTEST iterable is exhausted
# a different function called zip_longest works until the LONGEST iterable is exhausted
# NOTE: for shorterst list when it runs out, just inserts None values
daily_data = list(itertools.zip_longest(nums, range(10)))
print(daily_data)


print("-------------------- CYCLE --------------------")
# we can define a function to cycle through some number list
cycler = itertools.cycle([1, 2, 3, 'again...'])
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))  # again...
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))  # again...


# we could build a simple on/off switch
cycler = itertools.cycle(['on', 'off'])
print(next(cycler))
print(next(cycler))
print(next(cycler))


print("-------------------- REPEAT --------------------")
# we can also repeat some value
repeater = itertools.repeat(2, times=10)
# print(next(repeater))
# print(next(repeater))
# print(next(repeater))
# print(next(repeater)) # throws an exception here (when I had times=3)

# this typically comes handy in situations where we use zip / map
squares = map(pow, range(10), repeater)
print(list(squares))

# a similar function but one that takes in tuples of arguments directly is starmap
squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])  # 0, 1, 4


print("-------------------- COMBINATIONS / PERMUTATION --------------------")
# combos = order does NOT matter
# perms = order DOES matter
# combinations_with_replacement = combox WITH replacement
# product = perms WITH replacement

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['corey', 'nicole']


# returns 6
results = itertools.combinations(letters, 2)  # 2 = n choose 2 = nC2
# for item in results:
# print(item)


# returns 12
results = itertools.permutations(letters, 2)
# for item in results:
#     print(item)

# returns 35 - matches if you check "permutations" in notes
# i = 0
results = itertools.combinations_with_replacement(numbers, 4)
# for item in results:
#     print(item, i)
#     i += 1


# returns 4**4 = 256
results = itertools.product(numbers, repeat=4)
# for item in results:
#     print(item)

# a practical example for this last one - we could use it to deal a deck of 52 cards.
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']


def card_gen():
    # GENERATOR APPROACH 1
    for r in ranks:
        for s in suits:
            yield (r, s)


card_gen = card_gen()
print([next(card_gen) for _ in range(10)])


# GENERATOR APPROACH 2
card_gen = ((r, s) for r in ranks for s in suits)
print([next(card_gen) for _ in range(10)])

# CARTESIAN PRODUCT APPROACH
card_gen = itertools.product(ranks, suits)
print([next(card_gen) for _ in range(10)])

print("-------------------- CHAIN --------------------")
# what if we wanted to combine many lists?
# combined = letters + numbers + names is possible but grossly inefficient because it copies each one
combined = itertools.chain(letters, numbers, names)
print(list(combined))

# a futher use-case for chain is to flatten a list of lists:
LoL = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
combined2 = itertools.chain.from_iterable(LoL)
print(list(combined2))

print("-------------------- SLICE --------------------")
# we can slice an iterator - eg here the iterator goes to 10 but we're slicing it till 5
result = itertools.islice(range(10), 5)  # only end point
result = itertools.islice(range(10), 1, 5)  # both start point and end point
result = itertools.islice(range(10), 1, 5, 2)  # start, stop, step
result = itertools.islice(range(10), 1, None)  # will go until forever (BE CAREFUL)
for item in result:
    print(item)

# why is this useful? because we might have an iterator that is too big to put into memory
# eg we might want to open a file that is too big to store in memory all at once
with open('dogz.txt', 'r') as f:
    # files themselves are iterators so we can do this
    header = itertools.islice(f, 3)

    # this allows us to iterate over just the first couple lines without loading the entire file into memory
    for line in header:
        # the end='' is there to prevent the print statement from inserting a new line after each one here
        print(line, end='')

# slice can be used to "tame" an inifinite list:
infinite = itertools.repeat('abc')
finite = itertools.islice(infinite, 10)
print(list(finite))

print("-------------------- SELECTORS --------------------")
# kinda similar to filter function


def if_even(i):  # define a filter
    if i % 2 == 0:
        return True
    else:
        return False


nums = [1, 2, 3, 4, 5]  # define a substrate

filtered_nums = filter(if_even, nums)  # apply
# for item in filtered_nums:  # also returns an iterator
#     print(item)


# now the selector. instad of passing a FUNCTION - we now pass a LIST. that's the difference with filter
selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)
# for item in result:
#     print(item)


# interestingly, itertools also has a filter function - but the reverse. it returns the ones that match FALSE
result = itertools.filterfalse(if_even, nums)
# for item in result:
#     print(item)

# another example where we use filterfalse to only return positives
only_positives = itertools.filterfalse(lambda x: x <= 0, [-1, 1, -2, 3])
print(list(only_positives))  # 1,3


# this next function DROPS VALUES out of the iterable as long as they're True, UNTIL THE FIRST FALSE


def lt_2(i):
    if i < 2:
        return True
    else:
        return False


result = itertools.dropwhile(lt_2, nums)
# for i in result:
#     print(i)


# thix next one is the opposite - it will RETURN VALUES UNTIL FIRST FALSE
result = itertools.takewhile(lt_2, nums)
for i in result:
    print(i)


print("-------------------- ACCUMULATE --------------------")
# does exactly what it sounds like - accumulates a running total for all the values it has seen
result = itertools.accumulate(nums)
# for i in result:
#     print(i )

# the default operator is addition, but we can change that to eg subtraction
result = itertools.accumulate(nums, operator.mul)
for i in result:
    print(i)

# we can get more creative - eg use min
nums = [5, 6, 7, 3, 4, 5, 6, 6]
result = itertools.accumulate(nums, min)
print(list(result))


# and still more creative with lambdas
result = itertools.accumulate(nums, lambda x, y: (x+y)/2)  # aka average
print(list(result))


# accumulat ecan be used to model any first-order recurrence relation
# a first order recurrence relation is one of the format s(i) = Ps(i-1) + Q.
# in other words, y = ax + b, where x is the previous y
# for comparison, Fibonacci is second order recurrence relation: s(i) = Ps(i-1) + Qs(i-2) + R
def first_order_recurrence(p, q, initial_val):
    # note how it doesn't matter that the list we pass ONLY HAS THE FIRST VALUE AS CORRECT. That's all we need!!
    return itertools.accumulate(itertools.repeat(initial_val), lambda x, _: x*p+q)


# now let's use the above to build a bunch of sequences
# evens
evens = first_order_recurrence(1, 2, 0)
print([next(evens) for _ in range(5)])
# odds
odds = first_order_recurrence(1, 2, 1)
print([next(odds) for _ in range(5)])
# threes
threes = first_order_recurrence(1, 3, 0)
print([next(threes) for _ in range(5)])

# all ones
ones = first_order_recurrence(0, 1, 1)
print([next(ones) for _ in range(5)])

# all twos
twos = first_order_recurrence(1, 0, 2)
print([next(twos) for _ in range(5)])

# alternating ones
alts = first_order_recurrence(0, -1, 1)
print([next(alts) for _ in range(5)])


# we can define second order recursion in a similar way
# reminder: s(i) = Ps(i-1) + Qs(i-2) + R
def second_order_recurrence(p, q, r, initial_values):

    # this is the tricky part. generate an intermediate tuple containing the 2nd value and the 3rd value (never 1st + 2nd because we at least need two to generate third)
    intermediate = itertools.accumulate(itertools.repeat(
        initial_values), lambda s, _: (s[1], p*s[1] + q*s[0] + r))
    # for fibs the above simplifies to: lambda: x, _: (s[1], s[1]+s[0])
    # or in other words: give me the 2nd value, and let me generate the third by adding together second and first
    # print(next(intermediate))  # 0 1
    # print(next(intermediate))  # 1 1
    # print(next(intermediate))  # 1 2
    # print(next(intermediate))  # 2 3
    # print(next(intermediate))  # 3 5

    # this is the simple part. always take the first value of the passed tuple = 0 1 1 2 3 5 8 13
    # would also work if we always took the second value [1] - would just be ahead by one iteration (would start from 1 not from 0)
    return map(lambda x: x[0], intermediate)


fibs = second_order_recurrence(p=1, q=1, r=0, initial_values=(0, 1))
print([next(fibs) for _ in range(10)])

alt_fibs = second_order_recurrence(p=-1, q=1, r=0, initial_values=(-1, 1))
print([next(alt_fibs) for _ in range(10)])

# a sister function to accumulate is reduce. It's very similar in that it performs an operation on all elements, BUT it returns a SINGLE element.
L = [1, 2, 3, 4, 5]
result = functools.reduce(operator.add, L)  # returns 1+2+3+4+5 = 15
print(result)


print("-------------------- GROUP BY --------------------")
# groups values based on key. returns a tuple with first value = key and second value = iterator with all the values that matched the key

people = [
    {'name': 'ilja', 'job': 'hacker'},
    {'name': 'ron', 'job': 'hacker'},
    {'name': 'tej', 'job': 'banker'},
    {'name': 'gio', 'job': 'banker'},
    {'name': 'mom', 'job': 'trader'}
]


def get_job(person):
    return person['job']


result = itertools.groupby(people, key=get_job)
for key, group in result:
    print(key, list(group))

# NOTE: it expects an already ORDERED list of people. Eg if you had another hacker right at the end the function would return them as a separate group.
# NOTE: if no key is specified, default grouping is done by identity


print("-------------------- COPYING AN ITERATOR --------------------")

# ==============================================================================
# SIMPLEST EXPLANATION OF TEE - https://www.youtube.com/watch?v=iYZdOobl4DE


def simple_gen():
    for i in range(10):
        yield i


simple = simple_gen()
# print(list(simple))
# print(list(simple))  # second comes back empty

# but if we split first
simple1, simple2 = itertools.tee(simple)
print(list(simple1))
print(list(simple2))  # both come back ok!


# ==============================================================================
# FIRTS - QUICK ASIDE FROM REAL PYTHON

print('---')
# try n split without the tee - DOES NOT WORK. We've iterated through the list once during first islice.
result = iter([1, 2, 3, 4, 5, 6])
# print(list(result))
n = 3
top = itertools.islice(result, n)
bottom = itertools.islice(result, n, None)
print(list(top))
# this comes back empty, because we've iterated through entire list once when we had to make the "top" copy
print(list(bottom))


print('---')
# try n split with the tee - THIS TIME WORKS!
result = iter([1, 2, 3, 4, 5, 6])
n = 3
# NOTE: tee takes in an iteraTOR. It could take an iteraBLE but that makes it pointless.
iter1, iter2 = itertools.tee(result, 2)
# when we extract value from first, we append it to the second one, which means we can then iterate over it
top = itertools.islice(iter1, n)
bottom = itertools.islice(iter2, n, None)
print(list(top))
print(list(bottom))


"""
While tee() is useful for creating independent iterators, it is important to understand a little bit about how it works under the hood.
When you call tee() to create n independent iterators, each iterator is essentially working with its own FIFO queue.

When a value is extracted from one iterator, that value is appended to the queues for the other iterators.
Thus, if one iterator is exhausted before the others, each remaining iterator will hold a copy of the entire iterable in memory.
(You can find a Python function that emulates tee() in the itertools docs.)

For this reason, tee() should be used with care. If you are exhausting large portions of an iterator before working with the other returned by tee(),
you may be better off casting the input iterator to a list or tuple.
"""


# ==============================================================================
# BACK TO COREY - THIS EXAMPLE IS MORE COMLICATED BECAUSE GROUPBY PRODUCES AN ITERATOR WITH GROUPS WITH A FURTHER ITERATOR NESTED INSIDE = GROUP[1]
result = itertools.groupby(people, key=get_job)

print('---')
# this produces nothing = can't iterate over same iterator twice
# for key, group in result:
#     print(key, list(group))

print('---')
# this produces nothing = can't copy an iterator into a sifferent variable and iterate again
# result2 = result
# for key, group in result2:
#     print(key, list(group))

print('---')
# this allows us to split the iterator into numerous ones, but we still can only iterate over all of them once

copy1, copy2, copy3, copy4, copy5 = itertools.tee(result, 5)

first_group = itertools.islice(copy1, 1)
second_group = itertools.islice(copy2, 1, 2)
third_group = itertools.islice(copy3, 2, None)

# NOTE: if you run the below 3 print statements, the ones after won't work!
# print(list(first_group))
# print(list(second_group))
# print(list(third_group))

for key, group in first_group:
    print(key, list(group))

for key, group in second_group:
    print(key, list(group))

for key, group in third_group:
    print(key, list(group))

"""
SO IMPORTANT CONCLUSION: itertools.tee does NOT work on NESTED iterators such as groupby
instead you need to list(group) first, before doing any operations on it.
see full reply here -> https://stackoverflow.com/questions/15450022/python-itertools-groupby-multiple-values
"""


print("-------------------- REAL PYTHON --------------------")
# THIS SECOND PART IS FROM REAL PYTHON
# WHERE THEY COVERED SAME MATERIAL AS COREY I ADDED IT ABOVE - OTHERWISE I ADDED IT HERE
# https://realpython.com/python-itertools/

# loosely speaking: itertools are functions that operate ON OTHER iteraTORS to make them more complex (and hopefully more useful)

# reminder: a list is an iteraBLE coz it has the __iter__() function
# a list can be converted into an iteraTOR when we put int through a for loop or when we call __iter__() on it directly:
L = [1, 2, 3, 4]
L_iter = (L.__iter__())
print(L_iter.__next__())

# python also has a few built-in iteraTOR functions:
print(zip(L, L).__next__())
print(map(abs, L).__next__())

# if we want to convert an iterator back into an iterable, we just have to list it:
print(list(zip(L, L)))

# since iteraTORS themselves are iteraBLES - we can call one iteraTOR on top of another:
print(map(len, zip(L, L)).__next__())
# the inner iterator returns a tuple
# the outer iterator picks up the tutple and returns its length
# both the inner and the outer have .__next__() and the inner feeds its to the outer


# iterators are primarily used for 2 reasons
# 1 - improving memory efficiency (via "lazy" evaluation)
# 2 - improving execution speed

print("-------------------- SEE POWER OF ITERS --------------------")
# consider the simple task of breaking up a list into groups, where n = size of group


def naive_grouper(list_, n):
    num_of_chunks = int(len(list_)/n)
    return [tuple(list_[i:i+n]) for i in range(num_of_chunks)]


def better_grouper(list_, n):
    # first we create n copies of the same iterator object (literally all pointing to the same memory address)
    iterator_objects = [iter(list_)] * n
    # then we zip them together. The iterator counter is one and the same so the first n objects put first n elements into first group, and the next zip starts from n+1
    return list(zip(*iterator_objects))


L = [1, 2, 3, 4, 5, 6]
n = 3
# print(naive_grouper(L, n))
# print(better_grouper(L, n)) # both return the same, but this one never has to store the entire list in memory


print("-------------------- $100 CHANGE --------------------")
# how many ways exist to make change to $100 using the below?
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

# all_combos = []
# for i in range(1, len(bills)+1):
#     combos = itertools.combinations(bills, i)
#     for combo in combos:
#         if sum(combo) == 100:
#             all_combos.append(combo)
# print(len(all_combos))
# print(len(set(all_combos)))

# now what if the problem was that you can use any number of bills?
# bills = [50, 20, 10, 5, 1]
# all_combos_w_replacement = []
# for i in range(1, 101):  # 101 because we could have 100 1 dollar bills
#     combos = itertools.combinations_with_replacement(bills, i)
#     for combo in combos:
#         if sum(combo) == 100:
#             all_combos_w_replacement.append(combo)
# print(len(all_combos_w_replacement))
# print(len(set(all_combos_w_replacement)))
# output = 343, but takes a while to calc because there are 96.5m combinations


print("-------------------- DEALING CARDS --------------------")
# this is just a copy paste of what we had above
# create the cards using product approach
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']
card_gen = itertools.product(ranks, suits)
# cards = list(card_gen)
# print(len(cards))
random.seed(1)


def shuffle_and_yield_cards(card_gen):
    cards = list(card_gen)
    random.shuffle(cards)
    for card in cards:
        yield card


shuffled_cards = shuffle_and_yield_cards(card_gen)
# print(list(shuffled_cards))


def cut_and_yield_cards(shuffled_deck, n):
    iter1, iter2 = itertools.tee(shuffled_deck)
    top = itertools.islice(iter1, n)
    bottom = itertools.islice(iter2, n, None)
    deck = itertools.chain(bottom, top)
    for card in deck:
        yield card


cut_cards = cut_and_yield_cards(shuffled_cards, 2)
# print(list(cut_cards))


def deal(deck, num_hands=2, hand_size=5):
    # create 5 pointers to the same generator object
    iters = [iter(deck)] * hand_size
    # print(iters)

    # take NUM_HANDS (eg 2) cards from each of HAND_SIZE (eg 5) iterators (pointer shifts each time so we are taking consecutive cards)
    # literally of the format ((1,2),   (1,2),   (1,2),    (1,2),    (1,2))
    tup_of_cards = [tuple(itertools.islice(i, num_hands)) for i in iters]
    # print(tup_of_cards)

    # the naive approach:
    # for i in range(num_hands):
    #     hand = []
    #     for tup in tup_of_cards:
    #         hand.append(tup[i])
    #     print(hand)

    # the cool way
    tup_of_hands = tuple(zip(*tup_of_cards))
    return tup_of_hands


hands = deal(cut_cards)
print(hands)
