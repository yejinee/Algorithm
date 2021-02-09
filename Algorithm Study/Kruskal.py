"""
[ 크루스칼 알고리즘 ]
- 동작과정
1) 간선 data를 비용에 따라 오름차순 정렬
2) 간선 1개씩 확인 하면서 현재 간선이 사이클 발생시키는지 check
    if 사이클 발생하는 경우 => 최소 신장 트리에 포함
    else: 최소 신장 트리에 포함 X
"""
# 특정 원소가 속한 집합을 찾는 function
def find_parent(parent, x):
    # 루트 노드 찾을때까지 찾아서 update
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# a,b속한 집합 합치기
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # 노드, 간선 갯수
parent = [0]*(v+1)  # 부모 table
# 부모 table 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

edges = []  # 간선 담는 list ( 비용, 간선 좌표)
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # cost 순으로 정렬하기 위해서 cost를 첫번째 원소로 설정
edges.sort()  # 비용에 따라 오름차순 정렬

result = 0  # 최종 비용
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 => 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
print(result)
