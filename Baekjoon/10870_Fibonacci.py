"""
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

[ input ]
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.


[output]
첫째 줄에 n번째 피보나치 수를 출력한다.


"""
# Solution 1 ) 재귀함수로 피보나치 수열 구하기
def findfib(n):
    if n<=1:
        return n 
    else:
        fib=findfib(n-1)+findfib(n-2)
        return fib

N=int(input())
print(findfib(N))



# Solution 2 ) 배열과 for문 이용해서 피보나치 수열 구하기
def findfib_iter(n):
    fiblist=[0,1]
    for i in range(2,n+1):
        fib=fiblist[i-1]+fiblist[i-2]
        fiblist.append(fib)

    return fiblist[n]    


N=int(input())
print(findfib_iter(N))

