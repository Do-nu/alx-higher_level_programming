#!/usr/bin/python3
a = 1
b = 2

def add(a, b):
    return (a + b)


print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]))
