# String Permutations:Print all the Permutations of a given string
from itertools import permutations 
t=int(input())
for i in range(t):
    stringInput=input()
    ans=list(''.join(z) for z in permutations(stringInput))
    print(*ans)
