n,k=(input().split())
n=int(n)
k=int(k)
value=[]
dp=[0 for _ in range(10000)]
dp[0]=1
for i in range(n):
    value.append(int(input()))

for i in value:
    for j in range(i,k+1):
       dp[j]+=dp[j-1] 

print(dp[k])