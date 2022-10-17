

def solution(S):
    cnt0, cnt1 = 0, 0
    if S[0]=='1':
        cnt0 += 1
    else:
        cnt1 += 1
    
    for i in range(len(S)):
        if S[i] != S[i-1]:
            if S[i]=='0':
                cnt1 += 1
            else:
                cnt0 +=1
    

    return min(cnt0, cnt1)
S = input()
print(solution(S))