# threading is beneficial when tasks are IO-bound. Downloading photos online is a great candidate!
# if tasks are doing a lot of number crunching on the CPU, less helpful - then need to use multi-processing

import send2trash
import os
import requests
import time
import threading
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f'sleeping {seconds} sec')
    time.sleep(seconds)
    return f'done sleeping... [slept for {seconds}] sec'


# NO THREADING
# do_something()
# do_something()


# SIMPLE THREADING
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()
# t1.join() # ensures both need finish before we move on
# t2.join()


# MORE INVOLVED THREADING
# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     # can't add the join method here because that would effectively concat all the threads into a single long one = effectively concurrency
#     # instead we'll have to apend them to a list of threads, and then have a second loop where we join them
#     threads.append(t)
#
# for t in threads:
#     t.join()


# # A NEWER WAY THAT WORKS SINCE PYTHON 3.2
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # submit method schedules a function to be executed and returns a futures object
#
#     # RUNNING A FEW
#     # f1 = executor.submit(do_something, 2.5)  # pass the function and the arg
#     # f2 = executor.submit(do_something, 2.5)
#     # print(f1.result())  # the future object contains the result we can now access
#     # print(f2.result())
#
#     # RUNNING MANY - YIELDING AS THEY COME
#     secs = [5, 4, 3, 2, 1]
#     # results = [executor.submit(do_something, 2.5) for _ in range(10)]
#     # results = [executor.submit(do_something, s) for s in secs]
#     # we can now use an iterator, which will yield results as they're completed
#     # NOTE that what this means for our exercise is that the one launched last (1,2s) will finishe before the ones launched early (5,4s)
#     # for f in concurrent.futures.as_completed(results):
#     # print(f.result())
#
#     # RUNNING MANY - YIELDING IN ORDER THEY WERE LAUNCHED
#     results = executor.map(do_something, secs)  # will run the function with every s in secs
#     for r in results:
#         print(r)
#     # NOTE how now now the results come 5-4-3-2-1, all at the same time (because 5 is longest and blocking others)
#
# finish = time.perf_counter()
# print(f'finished in {round(finish-start, 2)} seconds.')


# real world example with images
os.chdir('unsplash')
files = os.listdir()
for f in files:
    send2trash.send2trash(f)

urls = [
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg',
    'https://wallpapercave.com/wp/wp1814535.jpg'
]
# TIME
start = time.perf_counter()

# default - 43s
# for i, u in enumerate(urls):
#     res = requests.get(u)
#     res.raise_for_status()
#
#     print(f'downloading photo {i}')
#
#     with open(f'unsplash{i}.jpg', 'wb') as f:
#         for chunk in res.iter_content(100_000):
#             f.write(chunk)


# concurrent - 3.05s - holllyyyyyy sheeeeeetttttzzzzz
def download(url, i):
    res = requests.get(url)
    res.raise_for_status()

    print(f'downloading photo {i}')

    with open(f'unsplash{i}.jpg', 'wb') as f:
        for chunk in res.iter_content(100_000):
            f.write(chunk)

    return 'done with image {i}!'


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(download, url, i) for i, url in enumerate(urls)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

# TIME
end = time.perf_counter()
print(end-start)
