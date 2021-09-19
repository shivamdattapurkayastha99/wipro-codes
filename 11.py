# print the sorted non redundant occurences of elements from given input
# input:
# 1,3,5,6,2,3,5,5,4,3,2
# output:
# 1,2,3,4,5,6
numbers=list(map(int,input().split(",")))
numbers=set(numbers)
print(*numbers)
