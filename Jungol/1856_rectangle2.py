n, m =map(int, input().split()) #행 열 

for i in range(1,n+1):
    if i %2==0:    #짝수행 ->거꾸로 출력
        for k in range(m*i,m*(i-1),-1):
            print("%d"% k,end=" ")
    else:   # 홀수 행 -> 그대로 출력
        for k in range(m*(i-1)+1,m*i+1):
            print("%d"% k,end=" ")
    print()   
