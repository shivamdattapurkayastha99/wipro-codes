# Guess the operator
# given two integer a and b we need to perform an operation a#b where # can be any operator among these (+,-,*,/)
# perform an operation in such a way that a#b gets maximized
# return # in the form of the string
for _ in range(int(input())):
    a,b=map(int,input().split())
    res=[]
    for i in range(4):
        if i==0:
            res.append(a+b)
        if i==1:
            res.append(a-b)
        if i==2:
            res.append(a*b)
        if i==3:
            res.append(a/b)
    if res.index(max(res))==0:
        print('+')
    if res.index(max(res))==1:
        print('-')
    if res.index(max(res))==2:
        print('*')
    if res.index(max(res))==3:
        print('/')
        