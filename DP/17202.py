import sys
input = sys.stdin.readline



A = input()
B = input()
res = ''
for i in range(8):
	res += (str(A[i])+str(B[i]))
while len(res) > 2:
	tmp = ''
	for i in range(len(res)-1):
		tmp += str((int(res[i])+int(res[i+1]))%10)
	res = tmp
print(res)
		
