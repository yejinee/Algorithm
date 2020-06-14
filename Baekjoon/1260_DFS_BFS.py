"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

[ input ]
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.



[ output ]
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
 V부터 방문된 점을 순서대로 출력하면 된다.


"""


# 재귀함수 이용해서 해결
def DFS(v):
    print(v,end=' ')
    visit[v]=1
    for i in range(1,N+1):
        if visit[i]==0 and road[v][i]==1: # 경로가 연결되어있고, 방문 하지X node이면 
            DFS(i)


# Queue 이용해서 해결
def BFS(v):
    visited=[v] # 방문한 node
    queue=[v] 
    while queue:
        p=queue.pop(0)
        print(p,end=' ')
        for i in range(1,N+1):
            if i not in visited and road[p][i]==1:
                queue.append(i)
                visited.append(i)




N,M,V=map(int,input().split())
visit=[0]*(N+1)     #DFS - 방문한 node인지 알려주는 list ( 방문-1, 방문X-0)

# 경로를 행렬로 만들어 줘야함 N*N 행렬 - 인접행렬 통해 접근 
road=[[0]*(N+1)for i in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    road[x][y]=1
    road[y][x]=1

DFS(V)
print()
BFS(V)



