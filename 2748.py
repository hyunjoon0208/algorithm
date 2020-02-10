#피보나치 수2

n = int(input())

f0,f1=0,1
def fibo(n):
    global f0
    global f1
    for _ in range(n):
        f0,f1=f1,f0+f1

fibo(n)
print(f0)