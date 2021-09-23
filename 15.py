# maximum sum subarray(kadane's algo)
for _ in range(int(input())):
    a=list(map(int,input().split()))
    maxSum,maxSumUptilNow=0,0
    for i in a:
        maxSum+=i
        if maxSumUptilNow<maxSum:
            maxSumUptilNow=maxSum
        if maxSum<0:
            maxSum=0
    print(maxSumUptilNow)