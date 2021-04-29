"""
Q.10026 적록색약 
"""
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def findp(): # 적록색약이 아닌 사람 
    cnt=0
    check=[[0]*n for _ in range(n)] # 점 지나갔는지 CHECK 
    q=deque()
    for i in range(n):
        for j in range(n):

            if check[i][j]!=0: #이미 지나간 곳
                continue
            else:
                cnt+=1
                q.append([i,j])
                color=board[i][j]
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k] 
                        if nx>=0 and nx<n and ny>=0 and ny<n and check[nx][ny]==0 and color==board[nx][ny]:
                            check[nx][ny]=1
                            q.append([nx,ny])

    return cnt

def findp2(): # 적록색약이 아닌 사람 
    cnt=0
    check=[[0]*n for _ in range(n)] # 점 지나갔는지 CHECK 
    q=deque()
    for i in range(n):
        for j in range(n):
            if check[i][j]!=0:
                continue
            else:
                cnt+=1
                q.append([i,j])
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k] 
                        if nx>=0 and nx<n and ny>=0 and ny<n and check[nx][ny]==0:
                            if (board[nx][ny]=='R' and board[x][y]=='G') or (board[nx][ny]=='G' and board[x][y]=='R') or (board[nx][ny]==board[x][y]):
                                check[nx][ny]=1
                                q.append([nx,ny])
    return cnt


n=int(input())
board=[input() for _ in range(n)]
print(findp(),findp2())
