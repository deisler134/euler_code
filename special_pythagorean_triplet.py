'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a*a + b*b = c*c
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000
'''
import math
def special_pythagorean_triplet(circumference = 1000):
    for c in range(circumference//3+1,math.ceil(circumference/2)):
        for b in range((circumference - c)//2, c):
            a = circumference - b - c
            if c*c == a*a + b*b:
                print(a,b,c)

if __name__ == "__main__":
    special_pythagorean_triplet()