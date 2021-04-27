#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

[ input ]
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

[ output ]
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

"""


# In[ ]:


def solution(N,house):
    d=[[0]*3 for _ in range(N)]
    # initialize d
    for i in range(3):
        d[0][i]=house[0][i]
    for j in range(1,N):
        d[j][0]=min(d[j-1][1],d[j-1][2])+house[j][0]
        d[j][1]=min(d[j-1][0],d[j-1][2])+house[j][1]
        d[j][2]=min(d[j-1][0],d[j-1][1])+house[j][2]
    ans=min(d[N-1][0],d[N-1][1],d[N-1][2])
    return ans 


N=int(input())
house=[list(map(int,list(input().split()))) for _ in range(N)]
print(solution(N,house))

