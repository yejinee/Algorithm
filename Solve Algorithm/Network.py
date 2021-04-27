#!/usr/bin/env python
# coding: utf-8

# In[22]:


"""
프로그래머스 - 네트워크 
"""
from collections import deque

def solution(n, computers):
    q=deque()
    cnt=0
    beforenode=[] # 지나온 node 저장
    for i in range(n):
        # 지나간 적 있는 경우 
        if i in beforenode:
            continue
        cnt+=1
        q.append(i)
        while q:
            next=q.popleft()
            # 지나온 적 없는 경우 
            if next not in beforenode:
                for k in range(n):
                    # 연결되어있고 자기자신이 아니면
                    if computers[next][k]==1 and next!=k:
                        q.append(k)
                        beforenode.append(next)
    return cnt

