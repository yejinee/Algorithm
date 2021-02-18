"""
[ 다익스트라 알고리즘 ]
기존의 방법과 알고리즘은 유사하나 
Time Complexity의 개선을 위해 Priority Queue를 이용함 
=> 최소 Heap 자료구조 사용
"""
import heapq
import sys
imput=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)] # 각 노드에 연결되어있는 노드 정보 list 
distance=[INF]*(n+1)  # 최단거리 테이블 

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[] #heap 자료구조
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        # 최단거리 짧은 노드에 대한 정보 꺼내기
        dist, now=heapq.heappop(q)
        # 이미 지나간 노드인 경우
        if distance[now]<dist:
            continue
        # 인접 노드 확인 
        for i in graph[now]:
            cost=dist+i[1] # 현재 노드 거쳐서 갈때 
            # 현재노드 거쳐서 가는게 더 나은 경우 update
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("불가능")
    else:
        print(distance[i])