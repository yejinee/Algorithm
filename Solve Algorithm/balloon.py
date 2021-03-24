"""
[ 프로그래머스 - 풍선터트리기 ]
- solution
    (1) 양끝의 두개 숫자는 무조건 남을 수 있음
    (2) 양끝에서 출발해서 자기 자신보다 작은 숫자들은 남길 수 있음

"""

def solution(a):
    cnt=2 # 양쪽 끝
    left,right=a[0],a[-1]
    if len(a)>2:
        for i in range(1,len(a)-1):
            if left>a[i]:
                left=a[i]
                cnt+=1
            if right>a[-1-i]:
                right=a[-1-i]
                cnt+=1
        if right==left:
            cnt-=1
    return cnt
a=[-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))

b= [9,-1,-5]
print(solution(b))