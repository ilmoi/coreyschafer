import random

# betwen 0 and 1, 0 includive, 1 not
value = random.random()
print(value)

# between any two values
value = random.uniform(1, 10)
print(value)

# random integrers (includes both sides)
value = random.randint(1, 6)
print(value)

# select a random value from a list
greetings = ['hi', 'hello', 'howdy']
value = random.choice(greetings)
print(value)

# multiple choices
colors = ['red', 'black', 'green']
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

# randomly shuffle a list of values
deck = list(range(1, 53))
random.shuffle(deck)  # shuffles in place
print(deck)

# lets get 5 random cards from the deck
# choices wont work - can select the same card many times
# instead we're going to use the sample method
hand = random.sample(deck, k=5)
print(hand)
