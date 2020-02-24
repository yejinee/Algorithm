"""
Q) NO.2750 수 정렬하기 - 선택정렬로 해결

[Selection Sort]
-Time complexity: O(n)

: 기준이 되는 수와 나머지 수들을 비교해서 작은 수를 제일 앞으로 보내기

EX) 4 10 2 5 7
    2 10 4 5 7
    2 4 10 5 7
    2 4 5 10 7
    2 4 5 7 10
    

[INPUT]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

[OUTPUT]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

[SOLUTION]
1. list의 [0]을 기준으로 나머지 원소들과 크기 비교
2. 기준보다 작은 원소 - 존재하면 원소 바꾸기
                      - 존재하지 않으면 기준을 고정시키고 
3. 새로운 기준 설정= [기준+1]

[RESULT]
[2, 10, 4, 5, 7]
[2, 4, 10, 5, 7]
[2, 4, 5, 10, 7]
[2, 4, 5, 7, 10]
[2, 4, 5, 7, 10]

"""
def Selectionsort(A):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                A[i],A[j]=A[j],A[i]
                print(A)
    return A

# Data 입력
N=int(input())
numlist=[]
for i in range(N):
    a=int(input())
    numlist.append(a)

result=Selectionsort(numlist)
print(result)
for i in result:
    print(i)

