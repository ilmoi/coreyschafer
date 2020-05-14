import json
import csv


# =====================================================
# works, direct to text
with open('quotes.json', 'r') as json_f:
    data = json.load(json_f)

    quote_list = []

    with open('quotes.txt', 'w') as text_f:
        for quote_object in data:
            quote = quote_object['Quote']
            if quote not in quote_list:
                text_f.write(f'{quote}\n')
                quote_list.append(quote)

# with open('short_quotes.txt', 'r+') as f:
#     txt = f.read()
#     print(txt)

# print(quote_list)


# =====================================================
# going through csv
# with open('quotes.json', 'r') as json_f:
#     data = json.load(json_f)
#
#     with open('short_quotes.csv', 'w+') as csv_f:
#         csv_writer = csv.writer(csv_f)
#         for quote_object in data:
#             quote = quote_object['Quote']
#             print(quote)
#             print('-----')
#             csv_writer.writerow([quote])


# with open('short_quotes.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for line in csv_reader:
#         print(line)


# =====================================================
# trying to read
# with open('short_quotes.json', 'r') as json_f:
#     data = json.load(json_f)
#
#     with open('short_quotes.txt', 'w+') as text_f:
#         for quote_object in data:
#             quote = quote_object['Quote']
#
#             print(text_f.read()) # prints nothing?
#             # if it can't read the doc, I can't check if quote already there
#
#             text_f.write(f'{quote}\n')
#
# with open('short_quotes.txt', 'r+') as f:
#     txt = f.read()
#     print(txt)
