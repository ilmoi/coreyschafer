# generator approach 1
# yield keyword is what makes it a generator
def square_number(nums):
    for i in nums:
        yield(i*i)
# the benefit is performance - you don't need to store a list before you return (which can get long!)

my_nums = square_number([1,2,3,4,5])
# notice how it doesn't return anything. we need to use next() to access
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# the next one would break

# list comprehension
my_nums_list = [x*x for x in [1,2,3,4,5]]
print(my_nums_list)

# generator approach 2
my_nums_generator = (x*x for x in [1,2,3,4,5])
print(my_nums_generator)
print(list(my_nums_generator))
