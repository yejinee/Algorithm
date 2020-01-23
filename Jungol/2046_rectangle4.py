"""
정사각형의 한 변의 길이 n과 종류 m을 입력받은 후 
다음과 같은 정사각형 형태로 출력하는 프로그램을 작성
1)           2)            3)                                             
1 1 1        1 2 3         1 2 3                                   
2 2 2        3 2 1         2 4 6                              
3 3 3        1 2 3         3 6 9                                 

"""

n,m=map(int,input().split()) # n:한변의 길이, m:종류

if m==1:   #종류1
   for i in range(1,n+1):
    for j in range(1,n+1):
        print("%d" %i,end=" ")
    print()
elif m==2:  #종류2
    for i in range(1,n+1):  #행 의미
        if i%2==0:
            for j in range(n,0,-1):
                print("%d" %j,end=" ")
        else:
            for j in range(1,n+1):
                print("%d" %j,end=" ")
        print()
else: #종류3
    for i in range(1, n+1):
        for j in range (1,n+1):
            print("%d"%(i*j),end=" ")
        print()


