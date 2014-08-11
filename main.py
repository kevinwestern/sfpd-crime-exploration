import csv
import os

hoods = {}

for file in os.listdir('data/'):
  with open(os.path.join('data/', file), 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = reader.next()
    for row in reader:
      hood = row[6]
      if hood in hoods:
        hoods[hood] += 1
      else:
        hoods[hood] = 1

print hoods