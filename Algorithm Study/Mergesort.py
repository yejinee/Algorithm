"""
Q) NO.2751 수 정렬하기2 -병합정렬로 해결

[Merge Sort]
-Time complexity: O(nlogn)
- Divide & Conquer

:입력으로 하나의 list 받고 두개의 배열로 계속 쪼개기
-> 합치기 

- 쪼개기
: list의 크기가 1일때까지 계속 반복

- 합치기
쪼개진 2개의 list에서 작은 값을 새로운 list에 넣기


Ex) 7 4 5 1 6 3  - Mergesort fuction process
      [7 4 5]       [1 6 3]
    [7]  [4 5]    [1]    [6 3]
 [7]    [4] [5]  [1]    [6]  [3]
 [7]     [4 5]   [1]      [3 6]  
     [4 5 7]         [1 3 6]
           [1 3 4 5 6 7]




Q. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

[INPUT]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

[OUTPUT]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

[SOLUTION]
1. 원소 갯수가 1개가 될때까지 계속해서 1/2로 나누기
2. 원소 갯수가 1개가 되면 다른것과 merge

- Merge Function Process : 
EX) A[4 5 7]   B[1 3 6]
      i          j
=> Use new list: C[]
(1) C[1]
  A[4 5 7]   B[1 3 6]
    i            j
(2) C[1 3]
  A[4 5 7]   B[1 3 6]
    i              j
(3) C[1 3 4]
  A[4 5 7]   B[1 3 6]
      i            j
(4) C[1 3 4 5]
  A[4 5 7]   B[1 3 6]
        i          j
(5) C[1 3 4 5 6]
  A[4 5 7]   B[1 3 6]
        i          j
(4) C[1 3 4 5 6 7]
  A[4 5 7]   B[1 3 6]
        i          j
- Mergesort Function Process: 
Ex) 7 4 5 1 6 3  
      [7 4 5]       [1 6 3]
    [7]  [4 5]    [1]    [6 3]
 [7]    [4] [5]  [1]    [6]  [3]
 [7]     [4 5]   [1]      [3 6]  
     [4 5 7]         [1 3 6]
           [1 3 4 5 6 7]

"""
def merge(A,B):
    C=[]
    a=0
    b=0
    while a<len(A) and b<len(B):
        if A[a]<B[b]:
            C.append(A[a])
            a+=1
        else:
            C.append(B[b])
            b+=1
    while a<len(A):
        C.append(A[a])
        a +=1
    while b<len(B):
        C.append(B[b])
        b+=1
    return C


def MergeSort(A):
    mid=len(A)//2
    if len(A)>1:
        leftlist=A[:mid]
        rightlist=A[mid:]
        leftlist=MergeSort(leftlist)
        rightlist=MergeSort(rightlist)
        return merge(leftlist,rightlist)
    return A


N=int(input())
numlist=[]
for i in range(N):
    num=int(input())
    numlist.append(num)    

result=MergeSort(numlist)
for i in result:
    print(i)


