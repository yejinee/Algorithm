"""
도미노 타일은 두 조각으로 나누어져 있었고, 각 조각은 정사각형이다. 
조각에는 1과 6사이의 숫자가 써져 있다.

타일은 N줄로 놓여져 있고, 홀수 줄에는 N개의 타일이, 짝수 줄에는 N-1개의 타일이 놓여져 있다. 
아래 그림은 (N=5)일 때 타일이 놓여져 있는 형태이다.


한 타일에서 다른 타일로 넘어가려면, 두 타일이 인접해야 한다. 
또, 같은 변을 공유하는 조각에 쓰여 있는 숫자가 같아야 한다.

과외맨은 반대편으로 넘어가기 위해서 첫 줄의 가장 첫 타일에서 마지막 줄의 가장 마지막 타일로 이동하는 가장 짧은 경로를 찾으려고 한다.

타일은 row-major order에 의해서 번호가 매겨져 있으며, 첫 번째 줄의 첫 타일의 번호는 1, 마지막 타일의 번호는 N이다. 
두 번째 줄에서 첫 타일의 번호는 N+1이고, 마지막 타일의 번호는 2*N-1이다.

첫 줄의 첫 타일로만 과외맨이 들어갈 수 있고, 마지막 줄의 마지막 타일위에 과외 노트가 놓여져 있다.

마지막 줄의 마지막 타일로 이동할 수 없는 경우가 존재할 수 있다. 이 경우에는 번호가 가장 큰 타일로 이동하면 된다.

[ input ]
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 500) 다음 줄부터 N*N-N/2줄(/는 정수 나눗셈이다)에는 두 양의 Ai와 Bi가 주어진다. 
(1 ≤ Ai, Bi ≤ 6, 1 ≤ i ≤ N * N - N / 2) 타일 i의 왼쪽에 쓰여 있는 숫자는 Ai, 오른쪽에 쓰여 있는 숫자는 Bi이다.

[ output ]
첫째 줄에 가장 짧은 경로의 길이 (타일의 개수)를 출력한다.
둘째 줄에는 경로 상의 타일의 번호를 공백으로 구분하여 순서대로 출력한다. 만약, 가장 짧은 경로가 여러 가지라면, 
아무거나 출력하면 된다.


"""
from collections import deque
import sys
input= sys.stdin.readline

# 짝수행에 있을때의 이동 방향
dx0=[-1,-1,0,0,1,1]
dy0=[-1,0,-1,1,-1,0]
# 홀수행에 있을때의 이동 방향
dx1=[-1,-1,0,0,1,1]
dy1=[0,1,-1,1,0,1]
# (nx,ny)칸이 존재하는지 확인
def ok(x,y,N):
    if x<0 or x>=N:
        return False
    # 짝수줄 0 ~ N-1
    if x%2==0:
        return 0<=y<N
    # 홀수줄 0 ~ N
    else:
        return 0<=y<N-1
# (x,y)->(nx,ny)가능한지 확인
def go(x,y,nx,ny):
    # (x,y) & (nx,ny)가 같은 행인 경우
    if x==nx:
        if y<ny: return a[x][y][1] == a[nx][ny][0]  # (x,y)-> (nx,ny)
        else: return a[x][y][0]==a[nx][ny][1] # (nx,ny)<- (x,y)
    # (x,y) & (nx,ny)가 다른 행인 경우
    else:
        # (x,y)가 짝수 행인 경우
        if x%2==0:
            if y==ny: # 오른쪽 대각선으로 이동한 경우 
                return a[x][y][1]==a[nx][ny][0]
            else: #왼쪽 대각선으로 이동한 경우
                return a[x][y][0]==a[nx][ny][1]
        # (x,y)가 짝수 행인 경우
        else:
            if y==ny: #왼쪽 대각선으로 이동한 경우
                return a[x][y][0]==a[nx][ny][1]
            else: # 오른쪽 대각선으로 이동한 경우 
                return a[x][y][1]==a[nx][ny][0]

# 타일 넘버 구하는 function
def tilenum(x,y,N):
    answer=(x//2)*(2*N-1)+y+1
    if x%2==1:
        answer+=N
    return answer


def solution(a,N):
    q=deque()
    check=[[False]*N for _ in range(N)] # 타일지나갔는지 check
    dist=[[0]*N for _ in range(N)] # 몇 번만에 갔는지
    via=[[-1]*N for _ in range(N)] # 어디서부터 이동해왔는지
    q.append((0,0))
    check[0][0]=True
    dist[0][0]=1

    while q:
        x,y=q.popleft()
        for k in range(6): # 6개의 방향으로 움직임
            if x%2==0: # 짝수줄인 경우
                nx=x+dx0[k]
                ny=y+dy0[k]
            else: # 홀수 줄인 경우
                nx=x+dx1[k]
                ny=y+dy1[k]

            if ok(nx,ny,N)==False: continue # (nx,ny)칸이 존재하는지 확인
            if go(x,y,nx,ny)==False: continue # (x,y)->(nx,ny)가능한지 확인 
            if check[nx][ny]: continue # 이미 지나간 곳인지 확인
            check[nx][ny]=True
            dist[nx][ny]=dist[x][y]+1
            via[nx][ny]=(x,y)
            q.append((nx,ny))

    # 타일 갯수 출력하기
    ## 최대한 마지막 타일로 이동 
    x=N-1
    y=N-1
    while not check[x][y]: # 지나간 곳 나올때 까지 뒤에서 부터 체크
        y-=1
        if y<0:
            x-=1
            y=N-1
            if x%2==1:
                y-=1

    print(dist[x][y]) #true일때의 dist값
    
    #이동 경로 출력 
    ans=[]
    while not (x==0 and y==0):
        ans.append((x,y))
        x,y=via[x][y]
    ans.append((x,y))

    while ans:
        print(tilenum(*ans[-1],N),end=' ')
        ans.pop()
    print()

# 입력
N=int(input())
a=[[] for _ in range(N)]
for i in range(N):
    if i%2==0:
        lim=N
    else:
        lim=N-1
    for j in range(lim):
        a[i].append(tuple(map(int,input().split())))

solution(a,N)
