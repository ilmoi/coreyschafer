import os

# print(os.getcwd())

# os.mkdir('osmodule')

# print(os.listdir())

home_path = os.environ.get('HOME')
print(home_path)
new_path = os.path.join(home_path, 'test.txt')
print(new_path)b
