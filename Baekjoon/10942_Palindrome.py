"""
명우는 홍준이와 함께 팰린드롬 놀이를 해보려고 한다.

먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.

각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며, 
명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.

예를 들어, 홍준이가 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.

S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
S = 3, E = 3인 경우 1은 팰린드롬이다.
S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.
자연수 N개와 질문 M개가 모두 주어졌을 때, 명우의 대답을 구하는 프로그램을 작성하시오.

[ input ]
첫째 줄에 수열의 크기 N (1 ≤ N ≤ 2,000)이 주어진다.
둘째 줄에는 홍준이가 칠판에 적은 수 N개가 순서대로 주어진다. 칠판에 적은 수는 100,000보다 작거나 같은 자연수이다.
셋째 줄에는 홍준이가 한 질문의 개수 M (1 ≤ M ≤ 1,000,000)이 주어진다.
넷째 줄부터 M개의 줄에는 홍준이가 명우에게 한 질문 S와 E가 한 줄에 하나씩 주어진다.


[ output ]
총 M개의 줄에 걸쳐 홍준이의 질문에 대한 명우의 답을 입력으로 주어진 순서에 따라서 출력한다. 
팰린드롬인 경우에는 1, 아닌 경우에는 0을 출력한다.

"""
import sys
input= sys.stdin.readline

# input
n=int(input())
numlist=list(map(int,input().split()))
d=[[0]*n for _ in range(n)] # 팰린드롬이면 1, 아니면 0

for i in range(n): # 길이 1일때 무조건 팰린드롬 
    d[i][i]=1
for i in range(n-1): # 길이가 2인 경우
    if numlist[i]==numlist[i+1]: # 2개의 문자가 같으면 1
        d[i][i+1]=1
for k in range(2,n): # 길이가 3이상인 경우 (k: 길이 의미)
    for i in range(n-k): # k->2~n이면 i-> 0~n-2까지 가능
        if numlist[i]==numlist[i+k] and d[i+1][i+k-1]:
            d[i][i+k]=1

M=int(input())
for i in range(M):
    S,E=map(int,input().split())
    print(d[S-1][E-1])
    