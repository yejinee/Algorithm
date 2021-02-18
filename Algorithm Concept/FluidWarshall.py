"""
[ 플로이드 워셜 Algorithm ]
- 문제 상황 
: 모든 노드에서 다른 모든 노드까지의 최단 경로 table

- 점화식 
: (a-> b)의 최단거리보다 (a->k->b)의 거리가 더 짧은지 check
=> Dab=min(Dab, Dak+Dkb)

- 구현
1. 최단거리 table 초기화(현 노드와 인접 노드 파악해서 초기화)
2. 1번 node 거쳐가는 경우 고려해 최단거리table 갱신
    => (Dab=min(Dab, Da1+D1b))
3. 모든 node에 대해 진행 

- Time Complexity
:  노드 갯수 N개일 때, N번의 단계 수행 ( 현재 node 거쳐가는 모든 경로 )
"""

INF=int(1e9)

n=int(input()) # node 갯수
m=int(input()) # 간선 갯수 

graph=[[INF]*(n+1) for _ in range(n+1)] # 2차원 그래프(무한으로 초기화)

# 각 간선 정보 입력받고 값으로 초기화
for _ in range(m):
    a,b,c=map(int,input().split()) # a에서 b로 가는 비용 c
    graph[a][b]=c

# 자기 자신으로 가는 비용은 0으로 초기화 
"""
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0
"""
for a in range(1,n+1):
    graph[a][a]=0

# 점화식에 따라 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 결과 출력 
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우
        if graph[a][b]==INF:
            print("불가능",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()