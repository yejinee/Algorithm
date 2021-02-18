"""
Q) NO.2751 수 정렬하기2 - 힙정렬로 해결

[Heap Sort]
-Time complexity: O(n^2)


: Heap 자료구조 사용


- Heap 자료 구조
: 우선순위 중심으로 정렬된 시퀸스 활용해야할 때 유용
  한 노드가 최대 2개의 자식노드를 가짐
  마지막 level 제외한 모든 레벨에서 노드들이 꽉 채워짐
  => 완전 이진 트리

Ex)            A
         B          C
    D       E    F      G
H       I


Q. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

[INPUT]
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
수는 중복되지 않는다.

[OUTPUT]
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


"""
# Min Heap
def heapify(A,i,heap_size):
  parent=i
  left=2*i+1
  right=2*i+2
  if left<heap_size and A[left]>A[parent]:
    parent=left
  if right<heap_size and A[right]>A[parent]:
    parent=right 
  if parent!=i:
    A[parent],A[i]=A[i],A[parent]
    heapify(A,parent,heap_size)

def heapsort(A):
  for i in range(len(A)//2-1,-1,-1):
    heapify(A,i,len(A))
  for i in range(len(A)-1,0,-1):
    A[0],A[i]=A[i],A[0]
    heapify(A,0,i) 

N=int(input())
numlist=[]
for i in range(N):
    num=int(input())
    numlist.append(num)    
heapsort(numlist)
print(numlist)