#쉬운 계단 수

import sys
sys.setrecursionlimit(10**6)

n = int(input())
result=[[0 for _ in range(10)] for _ in range(101)]

for i in range(1,101):
    for j in range(10):
        if i == 1:
            result[i][j]=1
        else:
            if j==0:
                result[i][j]=result[i-1][j+1]
            elif j==9:
                result[i][j]=result[i-1][j-1]
            else:
                result[i][j]=result[i-1][j+1]+result[i-1][j-1]


print(sum(result[n][1:10])%1000000000)