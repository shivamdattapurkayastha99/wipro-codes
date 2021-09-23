# find the given number is possible as a sum of two numbers from the given array
def sumOfVal(arr,value):
    s=set()
    for i in arr:
        if value-i in s:
            print(value-i,i)
        else:
            s.add(i)
arr=list(map(int,input().split()))
value=int(input())
sumOfVal(arr,value)