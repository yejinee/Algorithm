"""
영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.
모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 
클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 
또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 
화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

[ input ]
첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.


[ output ]
첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.


"""
from collections import deque

n = int(input())
q = deque()
dist = [[-1]*(n+1) for _ in range(n+1)]

# initialize
q.append((1, 0))
dist[1][0] = 0

while q:
    s, c = q.popleft()
    if dist[s][s] == -1:  # 화면 -> clipboard
        dist[s][s] = dist[s][c]+1
        q.append((s, s))
    if s+c <= n and dist[s+c][c] == -1:  # clipboard -> 화면 (s+c가 범위 넘어갈수도 있음 )
        dist[s+c][c] = dist[s][c]+1
        q.append((s+c, c))
    # remove emoticon -> -1 (s-1의 범위 0이상이어야함)
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c]+1
        q.append((s-1, c))

"""
< min함수 이용해서 못하는 이유 >
배열안에 탐색하지 않은 -1이 존재할 수도 있기 때문 
"""

ans = -1
# 우리가 구해야하는 값 : d[n][i]들중 제일 큰 값
for i in range(n+1):
    if dist[n][i] != -1:
        if ans == -1 or ans > dist[n][i]:
            ans = dist[n][i]
print(ans)
