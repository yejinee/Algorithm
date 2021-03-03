"""
[ 이코테 - 음료수 얼려 먹기]
N*M 크기의 얼음 틀이 있다. 
구멍이 뚫린 부분 : 0 , 칸막이 존재하는 부분 : 1
구멍 뚫려있는 부분끼리 상하좌우 붙어있으면 서로 연결된거임
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 갯수?

[ input ]
첫번째 줄에 얼음 틀의 세로 길이 N, 가로 길이 M이 주어짐 (1<=N,M<=1000)
두번째 줄부터 N+1번째 줄까지 얼음 틀의 형태 주어짐
구멍 뚫린 부분 =>0 , 아닌부분 =>1


[ output ]
한번에 만들 수 있는 아이스크림 갯수

[ solution ]
구멍 뚫린 부분에 아이스크림 얼릴 수 있으므로 구멍의 갯수 구하면 된다

"""
def dfs(x,y):
    # 범위 벗어나는 경우
    if x<=-1 or x>= n or y <= -1 or y >= m:
        return False
    # 그래프가 빈칸인 경우
    if graph[x][y]==0:
        graph[x][y]=1
        # 상하좌우에 대해서도 다 구멍 막아주기
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

cnt=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            cnt+=1
print(cnt)


