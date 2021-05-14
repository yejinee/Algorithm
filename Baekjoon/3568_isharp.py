## isharp
def solution(s):
    ans=[]
    # 변수형 분리하기 
    k=0
    while s[k] !=' ':
        k+=1
    common=s[:k]
    word=s[k:-1].split(',')

    # 추가 변수형 만들기
    for w in word:
        i=len(w)-1
        temp=''
        # 변수 나올때까지는 추가 변수형임 (알파벳)
        while not w[i].isalpha():
            # []는 세트임 
            if w[i]==']':
                temp+='[]'
                i-=2
                continue
            temp+=w[i]
            i-=1
        temp+=w[0:i+1]
        ans.append(common+temp)
    # 출력
    for j in ans:
        print(j+';')

s=input()
solution(s)