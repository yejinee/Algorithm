"""
[ 이코테 - 1이 될 때까지 ]
어떠한 수 N이 1이 될 때까지 2과정 중 하나를 반복 수행
1. N-1
2. N//k (나누어 떨어질때만)

N,K가 주어질 때 N==1될때까지 1번, 2번의 과정을 수행하는 최소 횟수

[ input ]
첫째줄에 N(2<=N<=100000), K(2<=K<=100000)이 공백으로 구분되며 자연수로 주어짐

[ output ]
N=1될때까지 수행해야하는 횟수

"""
def solution(n,k):
    cnt=0
    while n!=1:
        if n%k==0:
            n/=k
        else: 
            n-=1
        cnt+=1
    return cnt


n,k=map(int,input().split())
print(solution(n,k))