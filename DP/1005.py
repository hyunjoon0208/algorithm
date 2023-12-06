import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solve():
	pass



def main():
	T = int(input())
	for _ in range(T):
		n, k = map(int, input().split())
		D = list(map(int, input().split()))
		lst = [0] * n
		path = [[] for _ in range(n)]
		for _ in range(k):
			x, y = map(int, input().split())
			if lst[y-1] < D[x-1]:
				lst[y-1] = D[x-1]
			path[x-1] = y-1
		w = int(input())
		res = 0
		print(path)
		while True:
			res += lst[w-1]
			if path[w-1] == []:
				break
			w = path[w-1]
			print(w)
		print(res)

if __name__ == '__main__':
	main()