"""
삼각형의 높이 n과 종류 m을 입력받은 후 다음과 같은 
삼각형 형태로 출력하는 프로그램을 작성하시오.


< 처리조건 >
종류 1번의 숫자의 진행 순서는 처음에 왼쪽에서 오른쪽으로 
진행 한 후 방향을 바꾸어서 이를 반복한다.

1)           2)            3)                                             
1           0 0 0 0 0      1                                     
3 2           1 1 1        1 2                             
4 5 6           3          1      

"""

n,m =map(int,input().split())
if n<=100 and n%2!=0:
    if m==1:
        count1=1
        for i in range(1,n+1):
            if i%2==0:  #숫자 거꾸로
                count1=count1+i
                hcount=count1-1
                for j in range(1,i+1):
                    print("%d"%hcount, end=' ')
                    hcount=hcount-1
                print()	
            else:	#그대로
                for j in range(1,i+1):
                    print("%d"%count1,end=' ')
                    count1=count1+1
                print()
    elif m==2:
        count=0
        while count<n:
            for i in range((2*n)-1,0,-2):
                result=f'{count} '
                print(" "*((2*n)-1-i) + result*(i))
                count=count+1
    elif m==3:
        for i in range(1,n//2+2): #1-4
            for j in range(1,i+1):
                print("%d"%j, end=' ')
            print()
        for k in range(n//2,0,-1):
            for n in range(1,k+1):
                print("%d"%n, end=' ')
            print()
    else:
        print("INPUT ERROR!")
else:
     print("INPUT ERROR!")
