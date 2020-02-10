#부분수열의 합

N,S=input().split()
N=int(N)
S=int(S)

nums=list(map(int, input().split()))

result=0

def solve(index,sums):
    global result
    if index>=N:
        if sums==S:
            result+=1
        return
    solve(index+1,sums+nums[index])
    # print('a',index)
    solve(index+1,sums)
    # print('b',index)
solve(0,0)
if S:
    print(result)
else:
    print(result-1)
