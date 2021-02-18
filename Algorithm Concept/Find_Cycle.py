"""
[ 서로소 집합을 활용한 사이클 판별 ]
: 무방향 그래프 내에서 사이클 판별 가능

- 동작과정
1) 각 간선을 확인하면서 두 node의 루트노드 확인
        (1) 루트 노드가 서로 다르면 Union연산 수행
        (2) 루트 노드가 서로 같으면 Cycle 발생
2) 그래프의 모든 간선에 대해서 1번을 반복
=> 모든 간선을 다 확인해도 사이클 없으면 그래프 내에 사이클 없다는 의미
"""

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e =map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

cycle=False
for i in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union(parent,a,b)

if cycle:
    print("cycle발생")
else:
    print("Cycle 발생 X")