# set = like a list but removes all duplicate values

# great solution whenever you're trying to compare two lists for matching values
s1 = set([1, 2, 3, 4, 5, 6])
print(s1)

# if you want to create an empty set, you need to use:
s2 = set([])
# not
s3 = {}
# the latter will create an empty dictionary!

# add values
s2.add(1)
print(s2)
s2.update([1, 2, 3], s1)
print(s2)

# remove values
s2.remove(5)
print(s2)
# s2.remove(6) #throws a key error
s2.discard(6)  # does not throw an error

# intersection
s4 = set([4, 5, 6, 7, 8])
i2 = s4.intersection(s2)
print(i2)
i3 = s4.intersection(s2, s1)
print(i3)

# difference (but only shows elemes of s4 that are not in s2)
d1 = s4.difference(s2)
print(d1)

# difference (shows both ways)
d2 = s4.symmetric_difference(s2)
print(d2)

# USECASES
# remove duplicate values from a list - quickest way to do it
l1 = [1, 2, 3, 3, 3, 4]
l2 = list(set(l1))
print(l2)

# quickly find intersections of lists
members = ['ilja', 'vadim', 'andrew']
developers = ['ilja', 'corey']

both = set(members).intersection(developers)  # note we have to case one to a list but not both
print(both)

# they are super performant when it comes to membership tests - O(1) vs O(n)
if 'ilja' in members:
    print('yep, in the list = O(n)')
if 'ilja' in set(members):
    print('yep in the set = O(1)')

#####################
dogz = set([])
catz = set(['inko', 'more cats'])
dogz.add('haisch')
dogz.update(['inko', 'pushistik'])
dogz.remove('haisch')
dogz.discard('haisch')  # no error, even though he's no longer there
isection = dogz.intersection(catz)  # inko
diff1 = dogz.difference(catz)  # pushistik
diff2 = dogz.symmetric_difference(catz)  # pushistik, other cats
