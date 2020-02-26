"""
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…

이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 
지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

[INPUT]
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

[OUTPUT]
첫째 줄에 분수를 출력한다.

[SOLUTION]
1. line과 몇번째 수(alpha)인지 구하기 
=> line=홀수인경우) 아래부터 시작 
                    분자=> line부터 -1
                    분모=> 1부터 +1
                So, line-(alpha-1)/alpha
=> line=짝수인경우) 위부터 시작
                    분자=> 1부터 +1
                    분모=> line부터 -1
                    So, alpha/line-(alpha-1)                             

"""
X = int(input())
line, sumvalue = 1, 1
while sumvalue + line <= X:
    sumvalue += line
    line += 1
    print("line is")
    print(line)
    print(sumvalue)
    print()
alpha = X - sumvalue
print("alpha is")
print(alpha)
x, y = alpha + 1, line - alpha
if line % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))

