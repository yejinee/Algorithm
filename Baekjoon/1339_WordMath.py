"""
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
두 수의 합은 99437이 되어서 최대가 될 것이다.

N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

[ input ]
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 
둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 
단어는 알파벳 대문자로만 이루어져있다. 
모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 
서로 다른 문자는 서로 다른 숫자를 나타낸다.


[ output ]
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.

[ solution ]
본래 조합으로 해결하려 했으나 시간초과 일어남.
greedy의 방식으로 풀어보려함 
ABCD + EDASC 의 경우 E의 값에 가장 큰 9가 들어가야 함 
각 알파벳의 자리수(10진수의 값)을 dictionary에 저장해 문제 해결
"""
def solution(n,word):
    ans=0
    # dictionary에 알파벳의 자리수의 값 저장 
    # ABC+AD 인 경우 A=100+10, B=10, C=1, D=1 저장
    dic={}
    for i in range(n):
        for j in range(len(word[i])):
            if word[i][j] not in dic:
                dic[word[i][j]]=pow(10,len(word[i])-j-1) 
            else: 
                dic[word[i][j]]+=pow(10,len(word[i])-j-1)

    # dic에 저장한 값 기준으로 정렬( 큰 값이 앞으로 정렬)
    wordsort=sorted(dic.items(),key=lambda x: x[1],reverse=True)
    # wordsort의 앞에 있는 값부터 차례로 큰 수 들어가야함
    num=9
    for i in range(len(wordsort)):
        ans+=num*wordsort[i][1]
        num-=1
    return ans


n=int(input())
word=[input() for _ in range(n)]
print(solution(n,word))