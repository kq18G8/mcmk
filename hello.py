import sys

f = open("pypy.csv", "r")
data = f.read()
data_ = data.split("\n")

data__ = data_[3]

print(data__)

data___ = data__.split(",")

print(data___)

for d in data___:
    sys.stdout.write(str(int(d)+1))
    sys.stdout.write(",")

