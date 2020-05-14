from urllib.request import urlopen
import json

two_quote_string = '''
{
  "quotes": [
    {
     "Quote": "Dont cry because its over, smile because it happened.",
     "Author": "Dr. Seuss",
     "Tags": [
       "attributed-no-source",
       "cry",
       "crying",
       "experience",
       "happiness",
       "joy",
       "life",
       "misattributed-dr-seuss",
       "optimism",
       "sadness",
       "smile",
       "smiling "
     ],
     "Popularity": 0.15566615566615566,
     "Category": "life"
   },
     {
       "Quote": "Sasi.",
       "Author": "Dr. Zeuss",
       "Tags": [
         "attributed-no-source",
         "cry",
         "crying",
         "experience",
         "happiness",
         "joy",
         "life",
         "misattributed-dr-seuss",
         "optimism",
         "sadness",
         "smile",
         "smiling "
       ],
       "Popularity": 0.15566615566615566,
       "Category": "happiness"
     }
  ]
}
'''

# basically the big insight with json is that when python opens it it converts it to pythonian things
# json itself becomes dictionary
# [] become lists
# true becomes True
# etc


# ==========================================================================
# first lets try working with strings
data = json.loads(two_quote_string)  # loadS loads a string
for quote in data['quotes']:
    del quote['Author']
    del quote['Popularity']

# indent allows us to print in nicely stacked format, sort_true organizes alphabetically
# we're using dumpS coz were dumping to a string
new_s = json.dumps(data, indent=2, sort_keys=True)
# print(new_s)


# ==========================================================================
# now lets try working with files
with open('short_quotes.json', 'r') as json_f:  # load[no s] loads a file
    data = json.load(json_f)

    # because its a dict we can remove a value
    for object in data:
        del object['Author']
        del object['Tags']

    # write to a text file
    with open('short_quotes.txt', 'w') as text_f:
        for quote_object in data:
            quote = quote_object['Quote']
            text_f.write(f'123{quote}\n')

    # write to another json
    with open('new_short_quotes.json', 'w') as new_f:
        json.dump(data, new_f)  # we're using dump coz we're dumping to a csv


# ==========================================================================
# now lets try working with APIs
with urlopen('https://api.exchangeratesapi.io/latest') as response:
    source = response.read().decode()  # get and decode response
    print(type(source))
    data = json.loads(source)  # convert to json
    print(type(data))
    data_s = json.dumps(data, indent=2)  # convert to string to make it more readable
    print(type(data_s))
    print(data_s)
