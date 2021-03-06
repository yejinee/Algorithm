"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열


[ input ]

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)


[ output ]
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.



"""
def promising(n):
    if n==0:
        return True
    if s.count(s[n])!=1:
        return False
    return True

def find(n):
    if n==M:
        print(' '.join(map(str,s)))
    else:
        for i in range(1,N+1):
            s[n]=i
            if promising(n):
                find(n+1)
        s[n]=0
            

N,M=map(int,input().split())
s=[0]*M
find(0)

