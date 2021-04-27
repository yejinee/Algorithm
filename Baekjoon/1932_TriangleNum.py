#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
[ Baekjoon 1932. 정수 삼각형]
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 
삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

[input]
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

[output]
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

"""


# In[ ]:


def solution():
    d=[[0]*n for _ in range(n)]
    d[0][0]=tri[0][0]
    for i in range(1,n):
        d[i][0]=d[i-1][0]+tri[i][0]
        for j in range(1,len(tri[i])):
            d[i][j]=max(d[i-1][j-1],d[i-1][j])+tri[i][j]
    ans=max(d[n-1])
    return ans

n=int(input())
tri=[list(map(int,list(input().split()))) for _ in range(n)]
print(solution())

