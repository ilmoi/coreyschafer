import requests
import shutil
import zipfile

with zipfile.ZipFile('files2.zip', 'w') as my_zip:
    my_zip.write('dogz.txt')
    my_zip.write('add.log')

# if we wanted to also compress it:
with zipfile.ZipFile('files_compressed.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('dogz.txt')
    my_zip.write('add.log')

# now lets practice reading zip files
with zipfile.ZipFile('files2.zip', 'r') as my_zip:
    print(my_zip.namelist())  # this reads the names of the files in there
    my_zip.extractall('files_dir')


# next lets take a look at shutil module, which allows us to work with both zip files and shutil
# with shutil you can only zip entire directories

# to create
shutil.make_archive('another', 'zip', 'files_dir')  # name of archive, format, folder to archive

# o extract
shutil.unpack_archive('another.zip', 'another_folder')

# available formats are (from fastest/biggers to slowest/smallest):
# zip = zip file
# tar = uncompressed tar file
# gztar = gzip'ed tar file
# bztar = bzip'ed tar file
# xztar = xz'ed tar file < use this if you have to choose, aka the smallest

shutil.make_archive('anotherGZZZZ', 'gztar', 'files_dir')


# now lets actually get a file from online
r = requests.get('https://drive.google.com/uc?export=download&id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV')

with open('data.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())
