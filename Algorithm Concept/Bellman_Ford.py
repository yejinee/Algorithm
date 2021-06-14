import sys
input=sys.stdin.readline
INF=int(1e9)


def bf(start):
    dist[start]=0
    # N-1번 반복
    for i in range(n):
        # 매번 모든 간선 확인
        for j in range(m):
            current=edges[j][0]
            nextnode=edges[j][1]
            cost=edges[j][2]
            # 현재 간선 거쳐 다른 노드로 이동하는게 더 짧을 경우
            # dist[nextnode] : start에서 nextnode로 바로가는거
            # dist[current] : start에서 current거쳐서 nextnode로 가는거
            if dist[current]!=INF and dist[nextnode]>dist[current]+cost:
                dist[nextnode]=dist[current]+cost
                # n번째 라운드에도 값 갱신되면 음수순환 존재 
                if i==n-1:
                    return True
    return False



n,m=map(int,input().split())
edges=[] #간선에 대한 정보
dist=[INF]*(n+1)

#간선 정보
for _ in range(m):
    a,b,c=map(int,input().split())
    # a에서 b로 가는 비용이 c
    edges.append((a,b,c))

negative_Cycle=bf(1) #시작노드는 1번

if negative_Cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기위한 최단 거리 출력
    for i in range(2,n+1):
        # 도달할 수 없는 경우 
        if dist[i]==INF:
            print("-1")
        # 도달할 수 있는 경우 거리 출력
        else:
            print(dist[i])