import csv

# first using the common csv reader and writer

# with open('20jokes.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_names.csv', 'w') as new_csv_file:
#         csv_writer = csv.writer(new_csv_file, delimiter='-')
#
#         next(csv_reader)  # we're skipping over the first value (column title)
#
#         for line in csv_reader:
#             # print(line[1])  # line 1 allows us to select which column we want inside of each lien
#             csv_writer.writerow(line)


# now using the dictionary reader and writer
# gives us more control over how to manage columns
with open('20jokes.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_20_jokes.csv', 'w') as new_file:
        fieldnames = ['Joke', 'ID']  # note how we swapped these

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()  # we're spcifically choosing to write down the headers

        for line in csv_reader:
            # print(line['Joke']) # makes it much more readable what we're getting out!
            csv_writer.writerow(line)
