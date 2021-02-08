"""
[ 서로소 집합 자료 구조 ]
- 연산 
1) 합집합 (Union)
- 동작과정
        1. Node 갯수 크기의 부모테이블 초기화 (자기 자신)
        2. Union하려는 node들의 루트노드 찾기 (부모테이블 거슬러 올라갈 것)
        3. 2개 node의 루트노트 중 더 작은 번호의 루트를 가진 노드의 루트노드가 다른 노드의 부모노드 됌   
        => 연결성 통해 집합의 형태 확인 가능( 재귀함수로 루트노드 확인해보아야함 )
2) 찾기 (Find)
: 경로 압축 방법(Find함수 재귀호출 뒤에 부모table 값 바로 갱신) 사용
"""
# 노드 X의 루트 노드 찾는 Function
def find_parent(parent,x):
    if parent[x] != x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# Union연산 수행하는 Function
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a

    else:
        parent[a]=b
    print(parent)

v,e=map(int,input().split())
parent=[0]*(v+1) #부모 table 초기화

# 부모 테이블의 부모를 자기자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

# Union 연산 수행하기
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

print("각 원소가 속한 집합", end=' ')
for i in range(1,v+1):
    print(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력
print("부모 테이블: ", end=' ')
for i in range(1,v+1):
    print(parent[i],end=' ')

