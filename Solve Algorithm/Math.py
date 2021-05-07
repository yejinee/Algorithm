def solution(answers):
    no1=[1,2,3,4,5]  # 1번 => 12345 
    no2=[2,1,2,3,2,4,2,5] # 2번 => 21232425
    no3=[3,3,1,1,2,2,4,4,5,5] # 3번 => 3311224455 
    countans=[0]*3
    rans=[]

    for i in range(len(answers)):
        if answers[i]==no1[i%len(no1)]:
            countans[0]+=1
        if answers[i]==no2[i%len(no2)]:
            countans[1]+=1
        if answers[i]==no3[i%len(no3)]:
            countans[2]+=1
    # 가장 많이 맞추는 사람 
    for i in range(len(countans)):
        if countans[i]==max(countans):
            rans.append(i+1)
    return rans
            
ans=[1,3,2,4,2]
print(solution(ans))
