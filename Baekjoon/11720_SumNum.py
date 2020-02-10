"""
N개의 숫자가 공백 없이 쓰여있다. 
이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

[INPUT]
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 
둘째 줄에 숫자 N개가 공백없이 주어진다.

[OUTPUT]
입력으로 주어진 숫자 N개의 합을 출력한다.

"""
# String으로 입력받기
N=int(input())
Num=input()

numlist=[]
# String을 Int형으로 바꿔서 list에 저장
for i in range(N):
    number=int(Num[i])
    numlist.append(number)
print(sum(numlist))



