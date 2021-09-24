# finding the disalike
def ans(a):
    z=[int(n)&1 for n in a]
    i=z.index(sum(z)==1)+1
    print(i)
    


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans(a)
