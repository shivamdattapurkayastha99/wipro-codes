# roots of the quadriatic equation

def ans(a,b,c):
    d=b**2-4*a*c
    if d>0:
        return "real"
    if d==0:
        return "equal"
    if d<0:
        return "imaginary"

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print(ans(a,b,c))
