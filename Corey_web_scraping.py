import re
from bs4 import BeautifulSoup
import requests
import csv

print("-------------------- BS4 BASICS --------------------")
# res = requests.get('https://www.youtube.com/watch?v=ng2o98k983k&t=2s')
res = requests.get('https://www.flickr.com/search/?text=doge')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# make it nice to look at
print(type(soup))
string_soup = soup.prettify()
print(type(string_soup))  # note - this turns it into a string
# print(soup)

print("-------------------- FIND / FIND ALL --------------------")
# find = returns the first object of a kind (and all of its insides)
match = soup.find('div')
print(match)

# we can navigate inside of what we found like this:
global_nav_shim = match.div.div.div.div
print(global_nav_shim)

# we can get more specific:
# (NOTE: the reason we use class_ not class is because class is a reserved keyword in python)
# match = soup.find('div', class_="main search-photos-results")
# ALTERNATIVE SYNTAX: RETURNS A LIST OF ALL ELEMENTS, NOT JUST ONE.
match = soup.findAll('div', {'class': 'main search-photos-results'})
# if you get the list back, need to do [0] // also note this converts to a STRING!
match = match.prettify()
with open('save_match4.html', 'w') as f:
    f.write(str(match))

# findAll = returns all objects
# eg here I'm saving ALL THE DIVS FROM THE FILE
match = soup.findAll('div')
with open('save_all_divs.html', 'w') as f:
    for m in match:
        f.write(m.prettify())

# now lets findAll images and loop through them
all_pics = soup.findAll('div', {'class': "view photo-list-photo-view requiredToShowOnServer awake"})
print(len(all_pics))  # fucking weird, it only finds 22 out of 130
for pic in all_pics:
    print(pic['style'])

print("-------------------- practice --------------------")
# let's practice with corey's own website
res = requests.get('https://coreyms.com/')
res.raise_for_status()
source = res.text
soup = BeautifulSoup(source, 'lxml')
print(len(soup))

# I was surprised that article is an HTML tag but then I discovered there were actually 100s of different tags -> https://way2tutorial.com/html/tag/index.php
with open('coreys_scraped_articles.csv', 'w') as csv_f:
    csv_writer = csv.writer(csv_f)
    csv_writer.writerow(['headline', 'summary', 'video_link'])

    for article in soup.findAll('article'):
        # print(article.prettify())

        # note you don't have to put in EVERY parent tag. Just the ones that differentiate - so eg if the thing you're looking for is the first link, you could directly do article.a.text (first a will be returned)
        headline = article.h2.a.text
        print(headline)

        # now let's get the actual post text
        summary = article.find('div', class_='entry-content').p.text
        print(summary)

        try:  # had to pass this as some articles may not eg have an iframe
            # now let's get the video link from the embedded video (iframe)
            # we can access attributes as if it was a dictionary
            iframe = article.find('iframe')['src']
            vid_id = iframe.split('/')[4].split('?')[0]
            yt_link = f'https://youtube.com/watch?v={vid_id}'
        except:
            yt_link = None

        print(yt_link)

        print('')

        csv_writer.writerow([headline, summary, yt_link])
