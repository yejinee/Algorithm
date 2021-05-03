"""
Q 17144. 미세먼지

"""
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def spreadust(x,y,boards):
    temp=[[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if boards[i][j]>0: 
                share=boards[i][j]//5
                cnt=0
                for k in range(4):
                    nx,ny=i+dx[k],j+dy[k]
                    if (nx>=0 and nx<r) and (ny>=0 and ny<c):
                        if boards[nx][ny]>=0:
                            temp[nx][ny]+=share
                            cnt+=1
                temp[i][j]+=(boards[i][j]-share*cnt)
            else:
                temp[i][j]+=boards[i][j]
    return temp



def aircleaner(x,y,b): #공청기의 위치 넣기
    #up[0]=>x-1
    temp1=b[x-1][c-1]
    for i in range(c-1,1,-1):
        b[x-1][i]=b[x-1][i-1]
    b[x-1][1]=0
    
    temp2=b[0][c-1]
    for i in range(x-2):
        b[i][c-1]=b[i+1][c-1]
    b[x-2][c-1]= temp1

    temp3=b[0][0]
    for i in range(c-2):
        b[0][i]=b[0][i+1]
    b[0][c-2]=temp2

    for i in range(x-2,1,-1):
        b[i][0]=b[i-1][0]
    b[1][0]=temp3


    t1=b[x][c-1]
    for i in range(c-1,1,-1):
        b[x][i]=b[x][i-1]
    b[x][1]=0

    t2=b[r-1][c-1]
    for i in range(r-1,x+1,-1):
        b[i][c-1]=b[i-1][c-1]
    b[x+1][c-1]=t1

    t3=b[r-1][0]
    for i in range(c-2):
        b[r-1][i]=b[r-1][i+1]
    b[r-1][c-2]=t2

    for i in range(x+1,r-1):
        b[i][0]=b[i+1][0]
    b[r-2][0]=t3

    return b
    
def solution(t,board):
    ans=0
    # x,y위치 구해주기 
    for i in range(r):
            if board[i][0]==-1:
                x=i+1
                break
    
    # t초간 반복 
    for time in range(t):
        nb=spreadust(x, 0, board)
        board=aircleaner(x, 0, nb)

    for i in range(r):
        ans+=sum(board[i])
    return ans+2

r,c,t=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(r)]
print(solution(t,b))