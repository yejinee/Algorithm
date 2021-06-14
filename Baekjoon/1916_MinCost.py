"""
[ Q1916. ]
N개의 도시가 있다. 
그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 
도시의 번호는 1부터 N까지이다.

[ input ]
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 
그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 
출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

[ output ]
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

"""
INF=1e9

def solution(n,m,info,start,end):
    dist[start]=0
    for i in range(n):
        for j in range(m):
            current=info[j][0]
            nextnode=info[j][1]
            cost=info[j][2]
            # 거쳐가는 것과 그냥 가는 것중 더 짧은 거리 채택 
            if dist[current]!=INF and dist[nextnode]>dist[current]+cost:
                dist[nextnode]=dist[current]+cost
    # 원래는 cycle만들어지는지 체크 해야하지만 (문제에서 그런 경우의 수는 없다 햇으므로 안함)
    return dist[end]


n=int(input())
m=int(input())
info=[]
for _ in range(m):
    x,y,cost=map(int,input().split())
    info.append((x,y,cost)) 
start,end=map(int,input().split())
dist=[INF]*(n+1)

print(solution(n,m,info,start,end))