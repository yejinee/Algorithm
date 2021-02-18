"""
삼각형의 높이 n과 종류 m을 입력받은 후 다음과 같은 삼각형 형태로 출력하는 프로그램을 작성.

INPUT
삼각형의 크기 n(n의 범위는 100 이하의 자연수)과 종류 m(m은 1부터 3사이의 자연수)을 입력받는다.


OUTPUT
위에서 언급한 3가지 종류를 입력에서 들어온 높이 n과 종류 m에 맞춰서 출력한다. 
입력된 데이터가 주어진 범위를 벗어나면 "INPUT ERROR!"을 출력한다.

EXAMPLE
type1)           type2)             type3)                                                           
*                ***                |  *                                                
**               **                 | ***                                               
***              *                  |*****                                              

"""

n,m=map(int,input().split())
if n<=100:
    if m==1:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print('*',end='')
            print()

    elif m==2:
        for i in range(n+1,1,-1):
            for j in range(i,1,-1):
                print('*',end='')
            print()
    elif m==3:
        for j in range(1,n*2,2):
            print((' '*((2*n-1-j)//2))+('*'*j)) 
    else:
        print('INPUT ERROR!')

else:
    print('INPUT ERROR!')