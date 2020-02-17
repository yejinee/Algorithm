"""
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

[INPUT]
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

[OUTPUT]
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""
from collections import Counter

S=input()
upper_word=S.upper() #모두다 대문자로 변환
word=Counter(upper_word) #Dictionary형태로 만들어 줄것 

max_word=[]
# Dictionary item모두에 접근해서 max값들을 모두 새로운 list에 저장
for key,value in word.items():
    if value==max(word.values()):
        max_word.append(key)

    if len(max_word)>1:
        break

#max값이 하나면 값 출력, 여러개면 ? 출력 
if len(max_word)==1:
    print(max_word[0])
else:
    print('?')

