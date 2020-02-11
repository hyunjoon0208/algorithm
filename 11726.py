#2*n 타일링
import sys
sys.setrecursionlimit(10**6)
n = int(input())
results=[0]*n
def dp(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if results[n-1]:
        return results[n-1]
    else:
        results[n-1]=dp(n-1)+dp(n-2)
        return results[n-1]

print(dp(n)%10007)
