L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [5, 4, 3, 2, 1]


# 1 CONSTANT
def constant(L):
    return L[0]


# 2 LINAR
def linear(L):
    for i in L:
        return i


# 3 LOGARITHMIC = reduces size of input data at each step
# characteristic = need to be diving /2 somewhere
# eg with binary search we're cutting the input in half every time
def binary(value, L):
    left = 0
    right = len(L)
    middle = (right - left)//2
    if value == L[middle]:
        return value
    elif value <= L[middle]:
        return binary(value, L[left:middle])
    else:
        return binary(value, L[middle:right])
# NOTE: binary with copying the list would be loglinear!


# 4 LOGLINEAR
# characteristic = need to be diving /2 somewhere
# It is important to understand that an algorithm that must access all elements
# of its input data cannot take logarithmic time,
# as the time taken for reading input of size n is of the order of n.
# therefor algos where you (1)read the list, (2)do a log op on each elem = loglinear
def merge_sort(L):

    def merge(left, right):  # 3 while loops together give linear complexity (you iterate over all i + all j)
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2  # the breaking into 2 part gives log
        left = merge_sort(L[0:middle])
        right = merge_sort(L[middle:len(L)])
        return merge(left, right)


# 5 POLYNOMIAL (both below are n**2)
# characteristic = nested loops
def simple_quadratic(L):
    for x in L:
        for y in L:
            print(x*y)


def bubble_sort(L):
    swap = False
    while not swap:  # first n (while loop)
        swap = True
        for j in range(1, len(L)):  # second n (for loop)
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]
    return L


def selection_sort(L):
    suffix_start = 0
    while suffix_start < len(L):  # first n (while loop)
        for i in range(suffix_start+1, len(L)):  # second n (for loop)
            if L[i] < L[suffix_start]:
                L[i], L[suffix_start] = L[suffix_start], L[i]
        suffix_start += 1
    return L


# 6 EXPONENTIAL
# characteristic = recursion with 2 returns per line
# typically brute-force password crackers are exponential, because they have to try every combination
# eg if you're trying only lower case characters, and you want a password of length 7, then it'd be 26**7 combos
# fibs = also an example
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
# d = {0: 0, 1: 1}
# fib_efficient(10, d)


# 7 FACTORIAL
# heap's algo can be used to generate all possible permutations of n elements
# taveling salesman problem is another one with O(n!) (when brute forced)
def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    for i in range(n):
        heap_permutation(data, n-1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
# data = [1, 2, 3]
# n = len(data)
# print(n)
# heap_permutation(data, n)
