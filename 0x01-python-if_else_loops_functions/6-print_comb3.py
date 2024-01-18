#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i != j:
            if i == 8 and j == 9:
                break
            print("{}{}, ".format(i, j), end='')
print("89")
