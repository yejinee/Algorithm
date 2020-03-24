"""
재귀적인 패턴으로 별을 찍어 보자.
 N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을
크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.



[input]
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.



[output]
첫째 줄부터 N번째 줄까지 별을 출력한다.



"""
def drawstar(star):
    printstar=[]
    for i in range(3*len(star)): #행 의미
        if i//len(star)==1: #3으로 나눈 몫이 1일 때
            printstar.append(star[i%len(star)]+" "*len(star)+star[i%len(star)])
        else:
            printstar.append(star[i%len(star)]*3) 
    return printstar



star=["***", "* *", "***"]
N=int(input())
k=0
while N!=3:
   N= int(N/3)
   k+=1

for i in range(k):
    star=drawstar(star)
for i in star:
    print(i)