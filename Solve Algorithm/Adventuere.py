"""
[ 이코테 - 모험가 길드 ]
-풀이
우선 순위 : 공포도가 낮은 모험가
1) 오름차순으로 정렬하기
2) list 원소 하나씩 확인하면서 group에 포함된 모험가 수>=공포도 이면 한개의 그룹 완성

"""
def solution(fear,n):
    fear.sort()
    num=0
    group=0
    for i in fear:
        num+=1
        if i<=num:
            group+=1
            num=0
    return group


n=int(input())
fear=list(map(int,input().split()))
print(solution(fear,n))