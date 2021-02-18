"""
삼각형의 높이 n과 종류 m을 입력받은 후 다음과 같은 삼각형 형태로 출력하는 프로그램을 작성하시오. 

다음은 n이 5인 경우의 예시이다.

"""
# n: 높이 , m: 종류 
n,m= map(int,input().split())
if n<=100 and n%2!=0:
    if m==1:
        for i in range(1,n//2+2):
    	    print("*"*i)
        for j in range(n//2,0,-1):
            print("*"*j)	
    elif m==2:
        for i in range(1,n//2+2):
            print((" "*(n//2+1-i))+("*"*i))
        for j in range (n//2, 0,-1):
            print((" "*(n//2-j+1))+("*"*j))
    elif m==3:
        for i in range(n,0,-2):
    	    print((" "*((n-i)//2))+("*"*i))
        for j in range(3,n+1,2):
	        print((" "*((n-j)//2))+("*"*j))
    elif m==4:
        for i in range(n//2+1,0,-1):
            print((" "*(n//2+1-i))+ ("*"*i))
        for j in range(2,n//2+2):
            print((" "*(n//2))+("*"*j))
    else:
        print("INPUT ERROR!")
else:
    print("INPUT ERROR!")

