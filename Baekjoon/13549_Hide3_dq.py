"""
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

[input]
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

[ output ]
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

[ solution 2 ]
deque 이용해서 풀어주기
1. 순간이동 하는 경우 -> deque의 앞에 넣음 
2. 걷는 경우 -> deque의 뒤에 넣음 


"""
from collections import deque
MAX = 200000

n, k = map(int, input().split())
dq = deque()
dist = [-1]*MAX

#initialize
dq.append(n)
dist[n] = 0

while dq:
    x = dq.popleft()
    # 순간이동
    if x*2 < MAX and dist[x*2] == -1:
        dq.appendleft(x*2)
        dist[x*2] = dist[x]
    # 걷기 : x+1
    if x+1 < MAX and dist[x+1] == -1:
        dq.append(x+1)
        dist[x+1] = dist[x]+1
    # 걷기 : x-1
    if x-1 >= 0 and dist[x-1] == -1:
        dq.append(x-1)
        dist[x-1] = dist[x]+1
print(dist[k])
