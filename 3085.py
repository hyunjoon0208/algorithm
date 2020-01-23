N = int(input())
candy=[]
Max_candy=0
for i in range(N):
    candy.append(list(input()))

def count():
    global Max_candy
    for i in range(N):
        cnt=1
        for j in range(1,N):
            if(candy[i][j]==candy[i][j-1]):
                cnt+=1
            else:
                if Max_candy<cnt:
                    Max_candy=cnt
                cnt=1
    
        if Max_candy<cnt:
                    Max_candy=cnt
    for i in range(N):
        cnt=1
        for j in range(1,N):
            if(candy[j][i]==candy[j-1][i]):
                cnt+=1
            else:
                if Max_candy<cnt:
                    Max_candy=cnt
                cnt=1
        if Max_candy<cnt:
                    Max_candy=cnt
for i in range(N):
    for j in range(N-1):
        tmp=candy[i][j]
        candy[i][j]=candy[i][j+1]
        candy[i][j+1]=tmp
        count()
        tmp=candy[i][j+1]
        candy[i][j+1]=candy[i][j]
        candy[i][j]=tmp

        tmp=candy[j][i]
        candy[j][i]=candy[j+1][i]
        candy[j+1][i]=tmp
        count()
        tmp=candy[j+1][i]
        candy[j+1][i]=candy[j][i]
        candy[j][i]=tmp

print(Max_candy)






