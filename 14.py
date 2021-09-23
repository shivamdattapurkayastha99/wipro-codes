# print the pythagorean triplet
import math as m
for _ in range(int(input())):
    a,b=map(int,input().split(" "))
    print(a,b,m.floor(m.sqrt(a**2+b**2)))