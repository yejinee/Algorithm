"""
미키의 뒷마당에는 특정 수의 양이 있다. 
그가 푹 잠든 사이에 배고픈 늑대는 마당에 들어와 양을 공격했다.

마당은 행과 열로 이루어진 직사각형 모양이다. 
글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.

한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면, 두 칸은 같은 영역 안에 속해 있다고 한다. 
마당에서 "탈출"할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.

다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 
그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.

맨 처음 모든 양과 늑대는 마당 안 영역에 존재한다.
아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램을 작성하라.

[ input ]
첫 줄에는 두 정수 R과 C가 주어지며(3 ≤ R, C ≤ 250), 각 수는 마당의 행과 열의 수를 의미한다.

다음 R개의 줄은 C개의 글자를 가진다. 이들은 마당의 구조(울타리, 양, 늑대의 위치)를 의미한다.

[ output ]
하나의 줄에 아침까지 살아있는 양과 늑대의 수를 의미하는 두 정수를 출력한다.

"""
from collections import deque
import sys
input= sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(sx,sy):
    q=deque()
    q.append((sx,sy))
    check[sx][sy]=True
    cnt=[0,0] # 1개 영역의 늑대, 양의 수
    while q:
        x,y=q.popleft()
        if a[x][y]=='v': cnt[0]+=1 # 늑대일 때
        elif a[x][y]=='o': cnt[1]+=1 # 양일 때 

        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if nx<0 or nx>=R or ny<0 or ny>=C: continue
            if a[nx][ny]=='#': continue
            if check[nx][ny]: continue
            q.append((nx,ny))
            check[nx][ny]=True
    return cnt



def solution(r,c,a):
    d=[] # 각 영역에 양이 몇마리인지?
    # 영역 전체 탐색 
    for i in range(r):
        for j in range(c):
            if a[i][j]!='#' and check[i][j]==False: #벽이거나 이미 지나온 곳이 아니면 bfs진행
                d.append(bfs(i,j))
    v,o=0,0 # 늑대, 양의 수 
    for cnt in d:
        if cnt[0]>=cnt[1]: #늑대 승리
            v+=cnt[0]
        else: # 양 승리 
            o+=cnt[1]
    print(o,v)



R,C=map(int,input().split())
a=[input() for _ in range(R)]
check=[[False]*C for _ in range(R)]
solution(R,C,a)