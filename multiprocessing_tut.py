"""This is a follow up to the threading tutorial."""

import os
import multiprocessing
import time
import concurrent.futures
from PIL import Image, ImageFilter

start = time.perf_counter()


def do_something(i):
    print(f'sleeping for {i} sec')
    time.sleep(i)
    return f'done sleeping for {i} sec'


# SINGLE PROCESS
do_something()

# EXACTLY SAME AS THREADING...
# do a couple
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)
p1.start()
p2.start()
p1.join()
p2.join()

# do many
processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[2.5])
    p.start()
    processes.append(p)
for p in processes:
    p.join()

# do a couple using concurrency module
with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 2)
    print(f1.result())
    print(f2.result())

# do many
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [8, 7, 6, 5, 4, 3, 2, 1]
    results = [executor.submit(do_something, i) for i in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# do many + print results in the right order
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [8, 7, 6, 5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)  # returns results not a future object
    for r in results:
        print(r)  # returns alltogether because waiting for the firs (8s) one to complete

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds.')


# ==============================================================================
# real world project but this time for processing

os.chdir('unsplash')
files = os.listdir()

images = [f'unsplash{i}.jpg' for i in range(17)]
print(images)

# TIME
start = time.perf_counter()

size = (1200, 1200)  # what photos will be resized to

# normal time: 3.74s
# for img_name in images:
#     img = Image.open(img_name)
#
#     img = img.filter(ImageFilter.GaussianBlur(15))
#
#     img.thumbnail(size)
#     img.save(f'processed/{img_name}')
#     print(f'{img_name} was processed...')

# concurrent processing time - completes in 1.15s, so 3x quicker


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    return f'{img_name} was processed...'


with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(process_image, i) for i in images]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

# TIME
end = time.perf_counter()
print(end-start)

# CONCLUSION
# YOU WILL SEE SIGNIFICANT SPEED UPS FOR IO-BASED TASKS FROM THREADING
# YOU WILL SEE SIGNIFICANT SPEED UPS FOR CPU-BASED TASKS FROM MULTIPROCESSING
