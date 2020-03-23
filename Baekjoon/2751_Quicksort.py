"""
Q) NO.2751 수 정렬하기2 - 퀵정렬로 해결

[Heap Sort]
-Time complexity 
(1) Worst case= O(n^2)
(2) Average case = O(nlogn)

(1) pivot을 정하고 고정시키는 방식으로 정렬
(2) pivot을 기준으로 left, right부분으로 나눠서 이 과정을 반복 

- Partition process
: list에서 제일 첫번째 원소를 pivot으로 정하고 pivot을 고정시키는 과정

<순서>
1. i은 첫번째 원소, j는 마지막 원소 부터 시작 
2.
(1) i의 경우 : 하나씩 index을 늘려가면서 pivot보다 큰 값 나오면 stop
(2) j의 경우 : 하나씩 index를 줄여가면서 pivot보다 작은 값나오면 stop

3. 
IF i<j : i가 가리키는 값과 j가 가리키는 값을 서로 바꿈 
ELSE: pivot값과 j가 가리키는 값을 서로 바꾸고 pivot을 고정시킨다. 

"""


def partition(Arr,l,h):
    pivot=Arr[l]
    i=l
    j=h
    count=0
    while i<j:
        while Arr[i]<=pivot and i<h:
            i+=1
        while Arr[j]>=pivot and j>l:
            j-=1
        if i<j:
            Arr[i],Arr[j]=Arr[j],Arr[i]
    Arr[l], Arr[j]=Arr[j],Arr[l]
    return Arr,j


def quicksort(Arr,l, h):
    if l<h:
        Arr,fix=partition(Arr,l,h)
        quicksort(Arr,l,fix-1)
        quicksort(Arr,fix+1,h)



A=[15,22,13,27,12,10,20,25]
quicksort(A,0,len(A)-1)
print(A)

    