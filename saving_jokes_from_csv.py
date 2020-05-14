import csv

with open('shortjokes.txt', 'w') as f:

    with open('shortjokes.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            f.write(line[1])
            f.write("\n")
