import sys
import csv
import os

args = sys.argv

if len(args) < 3:
    print("Uso: python reader.py <src> <dst> <change1> ...")
    sys.exit()

src = args[1]
dst = args[2]
changes = args[3:]

if not os.path.isfile(src):
    print("Errore: file non trovato:", src)

    directory = os.path.dirname(src) or "."
    print("File nella directory:")

    for f in os.listdir(directory):
        print(f)
    sys.exit()

with open(src, newline="") as file:
    reader = list(csv.reader(file))

for change in changes:
    try:
        col, row, value = change.split(",")
        col = int(col)
        row = int(row)

        reader[row][col] = value
    except:
        print("Errore nel change:", change)

for row in reader:
    print(",".join(row))


with open(dst, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(reader)