"""
N개의 정수가 주어진다. 
이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

[INPUT]
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

[OUTPUT]
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

"""

# max,min 구하는 Function 
def solvemaxmin(A):
    max=A[0]
    min=A[0]
    for i in A:
        if i>max:
            max=i
        if i<min:
            min=i
    return min, max

N=int(input())
A=list(map(int,input().split( ))) #N개의 정수 A
min, max=solvemaxmin(A)
print(min,max)

