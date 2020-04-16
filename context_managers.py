import os
from contextlib import contextmanager

# option 1 - build a context manager using a class


class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('dogz.txt', 'r') as f:
    print(f.read())
    # whenever we exit (unindent) the block, that is when __exit__ is ran

print(f.closed)


# option 2 - build a context manager using a decorator
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f  # at this point we enter the indentation
    finally:
        f.close()  # teardown


with open_file('dogz.txt', 'r') as f:
    print(f.read())

print(f.closed)


# custom context manager
cwd = os.getcwd()  # good candidate for context manager
os.chdir('dir1')  # go in
print(os.listdir())  # do something
os.chdir(cwd)  # teardown

cwd = os.getcwd()
os.chdir('dir2')
print(os.listdir())
os.chdir(cwd)


print('-'*10)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('dir1'):
    print(os.listdir())

with change_dir('dir2'):
    print(os.listdir())
