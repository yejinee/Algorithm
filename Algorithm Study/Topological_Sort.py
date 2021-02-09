"""
[ 위상 정렬 ]
: 사이클 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열 
ex) 선수 과목을 고려한 학습 순서 설정

- 진입차수 & 진출차수
진입차수 : 특정 node로 들어오는 간선의 갯수 
진출차수 : 특정 node로 나가는 간선의 갯수 

- 동작과정 (Queue이용하기)
1) 진입차수=0인 모든 node를 Queue에 넣기
2) Queue가 빌때까지 반복하기
    -1) Queue에서 원소 꺼내서 나가는 간선 제거 (=연결된 node의 진입차수-1)
    -2) 새롭게 진입차수=0 되는 node를 Queue에 넣기
=> 각 node가 Queue에 들어온 순서가 위상정렬 수행결과

- 특징
1) DAG(Direct Acyclic Graph: 사이클 없는 그래프) 에서만 수행가능
2) 여러가지 답이 존재함 ( 한 순서에 여러개의 node를 Queue에 넣는 경우)
3) 모든 원소를 방문하기 전에 Queue가 빈다면 사이클이 존재한다고 판단
"""
from collections import deque

v, e = map(int, input().split())  # node, 간선 갯수
indgree = [0]*(v+1)  # 진입차수 0으로 초기화
graph = [[] for _ in range(v+1)]  # 각 노드에 연결된 간선 저장 list

# 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a->b 가능
    indgree[b] += 1  # b의 진입차수 증가 (a->b이므로)


def topology_sort():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indgree[i] == 0:  # 진입차수 0인 node 큐에 넣기
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        # 꺼낸 node와 연결된 node들의 진입차수에서 1빼기 (나가는 간선 제거)
        for i in graph[now]:
            indgree[i] -= 1
            if indgree[i] == 0:  # 새롭게 진입차수가 0되는 node 큐에 넣기
                q.append(i)
    for i in result:
        print(i, end=' ')


topology_sort()
