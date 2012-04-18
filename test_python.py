"""Test python module"""

import sys;

def func1():
    print("Hello!");

def func2(a):
    print(a+2);
    return a-2;

func1();

lst = [5, 6, 3, 6];
print("lst: ", lst);

for i in lst:
    print(func2(i));

a, b = 5, 1;

a, b = b, a + b;

print(a, b);

#print(sys.argv);

for i in sys.stdin.readlines():
	print(i.rstrip());