"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 
각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

[INPUT]
첫째 줄에 단어의 개수 N이 들어온다. 
N은 100보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에 단어가 들어온다. 
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.


[OUTPUT]
첫째 줄에 그룹 단어의 개수를 출력한다.

"""
# Word가 Groupword인지 확인하는 Fuction
# Groupword인 경우:1 , 아닌경우: 0 을 반환 
def WordChecker(word):
    newword=[]
    for i,v in enumerate(word):
         #새로운 단어의 경우 list에 추가
        if v not in newword: 
            newword.append(v)
        #중복이 있는 단어의 경우
        else: 
            # 바로 전단어와 중복인 경우는 넘어감 
            # But 따로 동떨어진 단어인 경우는 Groupword가 아님 
            if (i!=0) and (word[i]!=word[i-1]):
               return 0 
    return 1

# Data 입력하면서 동시에 Groupword가 맞는지 체크 
N=int(input())
count=0
for i in range(N):
    new=input()
    count+=WordChecker(new)

print(count)