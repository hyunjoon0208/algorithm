import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dp = [0] * 100001
dp[2] = 1
dp[4] = 2
dp[5] = 1
def solution(n):
	global dp
	for i in range(6,n+1):
		if dp[i-2] != 0 and dp[i-5] != 0:
			dp[i] = min(dp[i-2], dp[i-5]) + 1
		elif dp[i-2] != 0:
			dp[i] = dp[i-2] + 1
		elif dp[i-5] != 0:
			dp[i] = dp[i-5] + 1
		else:
			dp[i] = 0

def main():
	global dp
	n = int(input())
	solution(n)
	print(dp[n]) if dp[n] != 0 else print(-1)


if __name__ == '__main__':
	main()