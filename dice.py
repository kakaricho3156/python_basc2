import random

dice = int(input("サイコロの面の数は？"))
count = int(input("何回降りますか"))
empty = []

for i in range(1, count+1):
    empty.append(random.randint(1, dice))

print(empty)
