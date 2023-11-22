import sys
input = sys.stdin.readline



dp = [[0, 0] for _ in range(46)]
dp[0][0] = 1
dp[0][1] = 0
def solve(n):
	global dp
	for i in range(1,n+1):
		#print(dp[i-1][0], dp[i-1][1])
		dp[i][0] = dp[i-1][1]
		dp[i][1] = dp[i-1][0] + dp[i-1][1]

def main():
	global dp
	n = int(input())
	solve(n)
	print(dp[n][0], dp[n][1])
	
	
if __name__ == '__main__':
	main()