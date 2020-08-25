"""
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 
지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

[ input ]
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.


[ output ]
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 
항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

"""
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

N,M=map(int, input().split())
maze=[list(map(int,list(input()))) for _ in range(N)] # 미로의 모양(N*M) 

check=[[False]* M for _ in range(N)] # 길을 지나갔는지 아닌지 
dist=[[0]*M for _ in range(N)] # 가중치가 몇인지 
q=deque()
# initialize start point
q.append((0,0))
check[0][0]=True
dist[0][0]=1
while q:
    x,y=q.popleft()
    for i in range(4): # 4방향 살펴보기 
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if check[nx][ny]==False and maze[x][y]==1: #방문한 적 없고 연결 되어있음 
                q.append((nx,ny))
                check[nx][ny]=True
                dist[nx][ny]=dist[x][y]+1
print(dist[N-1][M-1])



