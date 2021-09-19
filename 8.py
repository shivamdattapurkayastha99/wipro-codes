# A digital machine generates binary data which consists of a string of 0s and 1s.
#  A maximum signal M, in the data, consists of the maximum number of either 1s or 0s appearing consecutively 
#  in the data but M can’t be at the beginning or end of the string.
#   Design a way to find the length of the maximum signal.....
size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)

for i in range(0,size):
    if arr[i]=='1':
        count=count+1
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)