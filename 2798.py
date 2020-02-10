#블랙잭

N,M=input().split()
N=int(N)
M=int(M)

cards=list(map(int,input().split()))

max_=0
tmp=[]
tmp.extend(cards)
for i in cards:
    sum_=0
    tmp.remove(i)
    for j in tmp:
        tmp.remove(j)
        for k in tmp:
            sum_=i+j+k
            if M>=sum_>max_:
                max_=sum_
        tmp.append(j)
    tmp.append(i)

print(max_)