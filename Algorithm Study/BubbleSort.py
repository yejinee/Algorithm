"""
Q) NO.2750 수 정렬하기 -버블정렬로 해결

[버블 정렬]
-Time complexity: O(n^2)

:1st 2nd 자료 비교 -> 2nd 3rd 자료 비교 ....
1회전이 끝나면 제일 큰 자료가 list의 맨 뒤로 이동 

EX) 7 4 5 1 3
    4 7 5 1 3
    4 5 7 1 3
    4 5 1 7 3
    4 5 1 3 7
    => 1회전 (다 하고 나면 제일 큰 값 7이 고정)

[INPUT]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

[OUTPUT]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

[SOLUTION]
1. 몇회전인지에 대해 생각(data갯수가 n개면 -> n-1번 반복)
    1st: n개가지고 회전 => 2nd: n-1개 가지고 회전 ....=> (n-1)th: 2개 가지고 회전
2. 1회전 안에서 모든 원소들 접근 
    : 2개씩 비교해봐서 작은 값이 앞으로 오게 하기


[RESULT]
[2, 3, 4, 1, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
[1, 2, 3, 4, 5]

"""
# Bubble Sort 
def BubbleSort(A):
    for i in range(len(A),1, -1):
        for j in range(1,i):
            if A[j-1]>A[j]:
                A[j-1],A[j]=A[j],A[j-1]
    return A


# Data 입력
N=int(input())
numlist=[]
for i in range(N):
    a=int(input())
    numlist.append(a)

result=BubbleSort(numlist)
for i in result:
    print(i)