"""
정사각형의 한 변의 길이 n을 입력받은 후 숫자로 된 정사각형 형태로 출력하는 프로그램

< 처리조건 > 
숫자의 진행 순서는 처음에 왼쪽 위에서 아래쪽으로 n만큼 진행 한 후 
바로 오른쪽 위에서 다시 아래쪽으로 진행하는 방법으로 정사각형이 될 때까지 반복

input -> output
   4   -> 1 5 9 13
          2 6 10 14
          3 7 11 15
          4 8 12 16
"""

n=int(input())
temp=0
count=1
for i in range(1,n+1):
    temp=count   
    for j in range(1,n+1): 
        print("%d" %temp, end=" ")  
        temp=temp+n  
    print()
    count=count+1 



