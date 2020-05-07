"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

[ INPUT ]
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

[ OUTPUT ]
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


"""
import sys 
input=sys.stdin.readline

# Promising 한지 (대각선, 열)
def promising(x):
    for i in range(x):
        if stack[i]==stack[x] or (x-i)==abs(stack[x]-stack[i]):
            return False
    return True


def Nqueens(x):
    global count 
    if x==N: # 끝까지 다 도달한 경우
        count+=1
    else:
        for i in range(N): # x번째 queen의 열 정하기 
            stack[x]=i 
            #primising한 경우 x+1번째 quuen에 접근 
            if promising(x): 
                Nqueens(x+1)


N=int(input())
stack=[0]*N # initialize the Stack
count=0
Nqueens(0)
print(count)

