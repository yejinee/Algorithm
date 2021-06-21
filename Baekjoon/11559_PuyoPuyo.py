from collections import deque
import copy
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def crush():
    global board
    check=[[False]*6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            route=[]
            q=deque()
            if board[i][j]=='.' :
                continue
            cnt=0
            q.append([i,j])
            while q:
                x,y=q.popleft()
                check[x][y]=True
                value=board[x][y]
                route.append([x,y])
                cnt+=1
                for k in range(4):
                    nx,ny=x+dx[k], y+dy[k]
                    if 0<=nx<12 and 0<=ny<6 and board[nx][ny]==value and check[nx][ny]==False:
                        q.append([nx,ny])
            if cnt>=4:
                for i in range(len(route)):
                    sx=route[i][0]
                    sy=route[i][1]
                    board[sx][sy]='.'


def push():
    global board
    for j in range(6):
        count=0
        for i in range(11,-1,-1):
            if board[i][j]=='.':
                count+=1
            elif count!=0:
                board[i+count][j]=board[i][j]
                board[i][j]='.'
    
    


def check(board,nboard):
    for i in range(12):
        for j in range(6):
            if board[i][j]!=nboard[i][j]: 
                return True
    return False



def solution():
    global board
    count=0
    while True:
        newboard=copy.deepcopy(board)
        crush()
        # 2개 보드가 다르고 push수행해야함
        if check(board,newboard): 
            count+=1
            push()
        # 2개 보드가 같아서 더이상 수행 불가
        else:
            break
    return count




 
board=[list(input()) for _ in range(12)]

print(solution())