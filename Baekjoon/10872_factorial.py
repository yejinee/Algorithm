"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

[input]
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.


[output]
첫째 줄에 N!을 출력한다.

"""
def factorial(N):
    factN=1
    if N>1:
        factN=N*factorial(N-1)
    return factN

N=int(input())
print(factorial(N))


"""
# for문으로 작성해보기 
def factorialfor(N):
    factN=1
    for i in range(1,N+1):
        factN*=i
    return factN


N=int(input())
print(factorialfor(N))
"""



