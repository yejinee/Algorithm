import sys
from collections import deque
MAX = 100001
def solution(n, k):
    visited = [-1] * MAX
    dq = deque()
    dq.append(n)
    visited[n] = 0

    while dq:
        x = dq.popleft()
        if x == k:
            return visited[x]
        else:
            # 우선순위 가져야함
            if (0<=x*2<MAX) and (visited[x*2]==-1):
                dq.append(2*x)
                visited[2*x] = visited[x]
            if (0<=x-1<MAX) and (visited[x-1]==-1):
                dq.append(x-1)
                visited[x-1] = visited[x]+1
            if (0<=x+1<MAX) and (visited[x+1]==-1):
                dq.append(x+1)
                visited[x+1] = visited[x]+1

n,k = map(int, input().split())
print(solution(n, k))

