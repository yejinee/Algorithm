"""
< No.1920 - 수 찾기 >

[문제]

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

 
[input]
첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1≤M≤100,000)이 주어진다. 
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수들의 범위는 int 로 한다.

[output]
M개의 줄에 답을 출력한다. 
존재하면 1을, 존재하지 않으면 0을 출력한다.


"""
#a에서 target 찾는 Function
def BinarySearch(a,low,high,target):
    if low>high:
        return 0

    mid=(low+high)//2
    if a[mid]==target:  #찾은경우
        return 1
    elif a[mid]<target: #찾는 값이 더 큰 경우
        low=mid+1
        return BinarySearch(a,low,high,target)
    else: #찾는 값이 작은 경우
        high=mid-1
        return BinarySearch(a,low,high,target)

# 입력하기
N=int(input())  #N
A=list(map(int,input().split( ))) #N개의 정수 A
M=int(input()) #Q 
lm=list(map(int,input().split( ))) # M개의 정수 lm

A.sort()
# 출력하기
for i in lm:
    print(BinarySearch(A,0,len(A)-1,i))


