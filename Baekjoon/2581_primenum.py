"""
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 
소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 
이들 소수의 합은 620이고, 최솟값은 61이 된다.

[input]
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다


[output]
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 
둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

"""
#소수를 찾는 Function
def checkprime(num):
    if num==1:  #1은 소수가 아님
        return 0
    for i in range(2,num):
        if num%i==0: #소수가 아닌경우
            return 0 
    return 1  #소수인 경우


# N~M까지의 소수를 모두 찾는 Function
def findprimenum(M,N):
    primenum=[]
    for i in range(M,N+1):
        if checkprime(i)==1: #소수이면 list에 저장
            primenum.append(i)
    return primenum


M=int(input())
N=int(input())


primenum= findprimenum(M,N)
# N ~ M사이에 소수가 하나도 없는 경우 -1 출력
if len(primenum)==0:
        print(-1)
# 소수가 있는 경우: 최솟값과 합 출력 
else:
    minvalue=primenum[0]
    sumvalue=sum(primenum)
    print(sumvalue)
    print(minvalue)
