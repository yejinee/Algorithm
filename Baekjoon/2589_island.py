"""
Q 2589 . 보물섬
"""
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):
    dist=[[0]*m for _ in range(n)]
    q.append([x,y])
    dist[x][y]=1
    temp=0
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny]=='L'and dist[nx][ny]==0:
                    dist[nx][ny]=dist[x][y]+1
                    temp=max(temp,dist[nx][ny])
                    q.append([nx,ny])
    return temp-1

def solution():
    ans=0
    for x in range(n):
        for y in range(m):
            if board[x][y]=='L':
                ans=max(ans,bfs(x,y))
    return ans


n,m=map(int,input().split())
board=[input() for _ in range(n)]
q=deque()

print(solution())

