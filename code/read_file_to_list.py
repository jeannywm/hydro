import csv
import pprint

myreader = csv.reader(open('GCveg_quad.csv'))

rows_we_like = []
for row in myreader:
    print row[7]
    if row[7].upper() in ['BARE', 'DUFF', 'OPWA', 'LI', 'LITR']:
         continue
    if row[7] == 'SAVI':
        row[7] = 'SAPA'
    rows_we_like.append(row)

pprint.pprint( rows_we_like)

writer = csv.writer(open('GCveg_clean.csv', 'w'))
for row in rows_we_like:
    writer.writerow(row)

myreader = csv.reader(open('TSveg_quad.csv'))

rows_we_like = []
for row in myreader:
    print row[11]
    if row[11].upper() in ['BARE', 'DUFF', 'OPWA', 'LI', 'LITR']:
         continue
    if row[11] == 'SAVI':
        row[11] = 'SAPA'
    rows_we_like.append(row)

pprint.pprint( rows_we_like)

writer = csv.writer(open('TSveg_clean.csv', 'w'))
for row in rows_we_like:
    writer.writerow(row)


