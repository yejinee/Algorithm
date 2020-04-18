"""
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 
그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. 
(이 위치는 가장 처음 큐에서의 위치이다.) 
이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

[ input ]
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. 
N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 
둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 
위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.


[ output ]
첫째 줄에 문제의 정답을 출력한다.

"""

from collections import deque

# 전체적인 Algorithm의 흐름나타내는 Function
def First(N,arr):
    count=0
    queue=deque([i for i in range(1,N+1)]) 
    for i in arr:
        if queue.index(i)<=(len(queue)//2): #arr의 원소가 queue의 중간보다 앞에 위치
            while queue[0]!=i:
                Leftmove(queue) #i가 나올때까지 Leftmove
                count+=1        
        else: # arr의 원소가 queue의 중간보다 뒤에 위치
            while queue[0]!=i:
                Rightmove(queue) #i가 나올때까지 Rightmove
                count+=1       
        queue.popleft()  #queue의 제일 앞 원소 pop
    return count


def Leftmove(arr):
    mid=arr.popleft()
    arr.append(mid)

def Rightmove(arr):
    mid=arr.pop()
    arr.appendleft(mid)


N,M=map(int, input().split())
p=list(map(int,input().split()))
print(First(N,p))
