import os
from datetime import datetime

# see what's inside a module you're not familiar with
# print(dir(os))

# print current working directory
print(os.getcwd())

# see files/folders in current directory / other directory
# print(os.listdir())  # lists here
# print(os.listdir('/'))  # lists in root
print(os.listdir('.py'))

# create folders
# os.mkdir('dir2/mkdir_folder')  # only creates top level
# os.makedirs('dir2/dir3/dir4/makedirs_folder')  # creates all the intermediate ones

# rename
# os.rename('dir2/dir2_file.txt', 'dir2/new_renamed_file.txt')

# lets find out when the file was last modified
mod_time = os.stat('dogz.txt').st_mtime  # but this gives unreadable time
print(datetime.fromtimestamp(mod_time))

# we can change directory
os.chdir('dir2')
print(os.getcwd())

# we can traverse a tree of folders and print out contents of ech one
# for dirpath, dirnames, filenames in os.walk('/Users/ilja/Dropbox/Corey/'):
#     print(f'current path is {dirpath}')
#     print(f'folders inside are {dirnames}')
#     print(f'files inside are {filenames}')
#     print('')

# we can work with environemntal variables
# we can read them
h = os.environ.get('HOME')
print(h)
# we can write them
file_path = os.path.join(h, 'Dropbox/Corey/dir2/joiningggggg.txt')
print(file_path)

with open(file_path, 'w') as f:
    f.write('hellooozzaa')

# check if a path exists
print(os.path.exists('/Users/ilja'))
print(os.path.exists('/Users/notilja'))

# separate the filename from the path
print(os.path.basename('/random/shit/all/over/filename.txt'))

# separate the foldername from the path
print(os.path.dirname('/random/shit/all/over/filename.txt'))

# get both the dirname and basename
print(os.path.split('/random/shit/all/over/filename.txt'))

# split the filename and the extention - much easier than trying to parse the extention using string splicing
print(os.path.splitext('/random/shit/all/over/filename.txt'))

# if somethign exists in a folder without an extention it can be confusing if its a file or a dir
print(os.path.isfile('new_renamed_file.txt'))
print(os.path.isdir('dir3'))
