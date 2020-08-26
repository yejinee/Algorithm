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

[ solution 1 ]
Queue 2게 이용해서 풀기
"""
from collections import deque
MAX = 200000
n, k = map(int, input().split())
nowq = deque()
nextq = deque()
d = [-1]*MAX
# check = [False]*MAX

nowq.append(n)
d[n] = 0
#check[n] = True

"""
while nowq:
    # nowq 채워주기
    x = nowq.popleft()
    if x*2 < MAX and check[x*2] == False:
        nowq.append(x*2)
        check[x*2] = True
        d[x*2] = d[x]
    if x+1 < MAX and check[x+1] == False:
        nextq.append(x+1)
        check[x+1] = True
        d[x+1] = d[x]+1
    if x-1 >= 0 and check[x-1] == False:
        nextq.append(x-1)
        check[x-1] = True
        d[x-1] = d[x]+1
    if not nowq:
        nowq = nextq
        nextq = deque()
"""


while nowq:
    # nowq 채워주기
    x = nowq.popleft()
    if x*2 < MAX and d[x*2] == -1:
        nowq.append(x*2)
        d[x*2] = d[x]
    if x+1 < MAX and d[x+1] == -1:
        nextq.append(x+1)
        d[x+1] = d[x]+1
    if x-1 >= 0 and d[x-1] == -1:
        nextq.append(x-1)
        d[x-1] = d[x]+1
    if not nowq:
        nowq = nextq
        nextq = deque()


print(d[k])
