"""
Q) NO.2750 수 정렬하기 -삽입정렬로 해결

[삽입 정렬]
-Time complexity: O(n^2)

: 필요할 때만 위치를 바꿈 
앞에 있는 수들이 정렬이 되어 있다고 가정
=> 선택한 수를 앞에다가 끼워넣음 

EX) 1 10 5 8 7 6 4 3 2 9
    IF 5의 차례인 경우 들어갈 수 있는 위치
    => _ 1 _ 10 5 8 .... => 총 2개    
    1 5 10 8 7 6 4 3 2 9
    1 5 8 10 7 6 4 3 2 9
    1 5 7 8 10 6 4 3 2 9
    ....

[INPUT]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

[OUTPUT]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

[SOLUTION]
1. 앞에 수들을 역순으로 비교
2. IF) 전 수가 더 크면 값을 서로 CHANGE
3. 자리가 알맞아 질때까지 계속 반복

[RESULT]
[2, 5, 3, 4, 1]
[2, 3, 5, 4, 1]
[2, 3, 4, 5, 1]
[2, 3, 4, 1, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
[1, 2, 3, 4, 5]

"""
# Insert Sort 
def insertsort(A):
    for index in range(1,len(A)):
        for j in range(index,0,-1): #현재 값부터 거꾸로 비교 
            if A[j]<A[j-1]: # 전 값이 더 큰 경우
                A[j],A[j-1]=A[j-1],A[j] # 값 바꾸기 
            else:
                break
    return A

# Data 입력
N=int(input())
numlist=[]
for i in range(N):
    a=int(input())
    numlist.append(a)
       
result=insertsort(numlist)

for i in result:
    print(i)
