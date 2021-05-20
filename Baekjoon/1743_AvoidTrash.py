"""
Q 1743 . 음식물 피하기

"""
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def solution(n,m,k,board):
    maxsize=0
    check=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if check[i][j]==1:
                continue
            if board[i][j]==1:
                size=0
                q=deque()
                q.append([i,j])
                while q:
                    x,y=q.popleft()
                    for direct in range(4):
                        nx,ny=x+dx[direct], y+dy[direct]
                        if 0<=nx<n and 0<=ny<m and board[nx][ny]==1 and check[nx][ny]==0:
                            size+=1
                            q.append([nx,ny])
                            check[nx][ny]=1
                maxsize=max(maxsize,size)
    return maxsize


n,m,k=map(int,input().split())
board=[[0]*m for _ in range(n)]

for _ in range(k):
    r,c=map(int,input().split())
    board[r-1][c-1]=1

print(solution(n,m,k,board))
