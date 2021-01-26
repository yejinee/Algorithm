"""
[ 다익스트라 알고리즘 ]
- 문제상황 : 1개의 node에서 다른 모든 node까지의 최단 경로
- 구현
1) 단계마다 방문하지 않은 노드 중 최단 거리 가장 짧은 노드 선택
2) 해당 노드 거쳐서 다른 노드에 방문할때의 거리 & 전에 구해놓은 거리 비교
"""
import sys
input=sys.stdin.readline
INF =int(1e9) # 무한을 의미하는 값 -> 10억

n,m = map(int,input().split()) # 노드갯수, 간선 갯수
start=int(input()) # 시작점
graph=[[] for i in range(n+1)] # 각 노드와 연결되어있는 노드에 대한 정보 (연결리스트 형태)
visited=[False]*(n+1) # 방문한 경우 True
distance=[INF]*(n+1) # 최단 거리 테이블 

# a번 노드에서 b번 노드로 가는 비용이 c
for _ in range(m):
    a,b,c= map( int, input().split())
    graph[a].append((b,c))

# table에서 최단 거리가 가장 짧은 노드의 번호 반환 
def get_small_node():
    min_value=INF
    idx=0 
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]: #최단거리 짧고, 방문 이력 X
            min_value=distance[i]
            idx=i
    return idx

def dijkstra(start):
    # 시작점 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1] # j[0] 까지 가는 value=j[1]
    # 시작노드 제외한 전체 노드
    for i in range(n-1):
        now=get_small_node() # 1. 최단거리 가장 작은 값 가진 노드
        visited[now]=True # 방문
        for j in graph[now]: # 현재 노드와 연결된 다른 노드 확인 
            cost=distance[now]+j[1] # 현 노드 거쳐서 다른 노드로 가는 거리
            if cost<distance[j[0]]: # cost값이 기존의 값보다 작으면 distance update 
                distance[j[0]]=cost

dijkstra(start)

for i in range(n-1):
    if distance[i]==INF:
        print("impossible")
    else:
        print(distance[i])

