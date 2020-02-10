#N과 M(2)

import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
visited=[False]*(n+1)
output = []
nums_list=[]
def dfs(depth, n, m):
    if depth == m:
        # print(' '.join(map(str, output)))
        out_str =' '.join(map(str,sorted(output)))
        # print(out_str)
        if out_str not in nums_list:
            nums_list.append(out_str)
        return

    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        output.append(i)
        dfs(depth+1, n, m)
        visited[i]=False
        output.pop()
dfs(0,n,m)

for i in nums_list:
    print(i)