#LCS
import sys

first=sys.stdin.readline().strip()
second=sys.stdin.readline().strip()

first_len=len(first)
second_len=len(second)

result=[[0 for _ in range(second_len+1)]for _ in range(first_len+1)]

for i in range(1,first_len+1):
    for j in range(1,second_len+1):
        if first[i-1]==second[j-1]:
            result[i][j]=result[i-1][j-1]+1
        else:
            result[i][j]=max(result[i-1][j],result[i][j-1])

print(result[-1][-1])