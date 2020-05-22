"""
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, 
fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

[ input ]
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다.
 N은 40보다 작거나 같은 자연수 또는 0이다.


[ output ]
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

"""
"""
def fibonacci(n):
    global count0,count1
    if n==0:
        count0+=1
        return 0
    elif n==1:
        count1+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
T=int(input())
for i in range(T):
    count0,count1=0,0
    N=int(input())
    fibonacci(N)
    print(count0,count1)
"""

def fibonacci(n):
    count0=[1,0] # 0을 사용하는 횟수 list
    count1=[0,1] # 1을 사용하는 횟수 list
    for i in range(2,n+1):
        count0.append(count0[i-1]+count0[i-2])
        count1.append(count1[i-1]+count1[i-2])
    return count0[n], count1[n]

T=int(input())
for i in range(T):
    N=int(input())
    sc0,sc1=fibonacci(N)
    print(sc0,sc1)