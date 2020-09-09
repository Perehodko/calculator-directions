import csv
import pandas as ps

# a = 'a'
b = [1, 2, 3, 4, 5, 6, 7, 8]
c = 3


with open('data1.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    # print('Headers: ', headers)


f = open('data1.csv')
r = csv.reader(f)
row0=next(r)
row0.append("a")
print(row0)

for item in r:
    for i in b:
        item.append(i)
    # print(item)

df = ps.read_csv("data1.csv", sep=",", engine="python")
print(df)

df['b'] = b

print(df)