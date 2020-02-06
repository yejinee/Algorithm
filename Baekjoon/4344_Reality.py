"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
당신은 그들에게 슬픈 진실을 알려줘야 한다.

[ INPUT ]
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 
N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

[ OUTPUT ]
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 
반올림하여 소수점 셋째 자리까지 출력한다.

"""
# Dataset 만들기 
C=int(input())
Allcase=[]
for i in range(1,C+1):
    case=list(map(int,input().split()))
    Allcase.append(case)


# Case별 Percentage 구하기
for i in range(0,C):
    case_sum=0
    case_avg=0
    count=0
    case_sum=sum(Allcase[i])-Allcase[i][0]
    case_avg=case_sum/Allcase[i][0]
    for j in range(1,Allcase[i][0]+1):
        if Allcase[i][j]>case_avg:
            count=count+1
    percentage=count/Allcase[i][0]*100
    print(("%.3f"%percentage)+"%")    
