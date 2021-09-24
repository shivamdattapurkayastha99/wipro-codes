# the packet stream player
# a stream of n packets arrive at a video player...
def ans(a):
    val=[]
    d=0
    flag=True
    l=len(a)
    for i in range(l):
        for j in range(l):
            x=a[i]+d
            if 2**(j+1)==x:
                val.append(2**j+1)
                d=0
            if 2**(j+1)==x:
                val.append(2**j)
                d=x-(2**j)
                break
    if d>0:
        i=1
        while flag:
            if d/(2**i)<1:
                val.append(2**(i-1))
                flag=False
            i+=1
    return max(val)
    



for _ in range(int(input())):
    
    a=list(map(int,input().split()))
    # print(ans(a))
    ans(a)


