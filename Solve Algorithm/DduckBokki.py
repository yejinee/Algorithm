"""
[ 이코테 - 떡볶이 떡 만들기 ]
1봉지에 들어가는 떡의 길이는 철단기로 잘라서 맞춤
높이H를 지정하면 줄지어진 떡을 한 번에 절단 
높이가 H보다 킨 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 X
손님이 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값 

[ input ]
첫째 줄에는 떡의 개수 N과 요청한 떡의 길이 M이 주어짐 (1<=N<=1000000, 1<=M<=2000000000)
둘째 줄에는 떡의 개별 높이 주어짐 

[ output ]
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값
 
"""


def solution(n, m, dduck):
    start = 0
    end = max(dduck)
    height = 0  # 자르는 높이
    while start <= end:
        total = 0  # 잘린 떡 길이의 합
        mid = (start+end)//2
        for i in dduck:
            # 떡의 길이>h인 경우
            if i > mid:
                total += (i-mid)
        # 잘린 떡의 길이 합>m인 경우
        if total >= m:
            height = mid
            start = mid+1
        else:
            end = mid-1
    return height


n, m = map(int, input().split())
dduck = list(map(int, input().split()))
print(solution(n, m, dduck))
