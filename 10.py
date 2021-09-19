# Given an integer matrix of size N x N. Traverse it in a spiral form.
n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))
    
rounds = n//2+n%2
for i in range(rounds):
    
    for j in range(i, n-i):
        print(m[i][j], end=' ')
    for j in range(i+1, n-i):
        print(m[j][n-1-i], end=' ')
    for j in reversed(range(i, n-1-i)):
        print(m[n-1-i][j], end=' ')
    for j in reversed(range(i+1, n-1-i)):
        print(m[j][i], end=" ")
