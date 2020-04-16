from collections import namedtuple

# define a named tuple once
Color = namedtuple('Color', ['red', 'green', 'blue'])

# create instances of the named tuple
random_color = Color(55, 155, 255)
white_color = Color(255, 255, 255)

# test!
print(random_color.red)
print(white_color.blue)
