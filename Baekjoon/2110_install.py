"""
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

[ input ]
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

[ output ]
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

"""
import sys
input = sys.stdin.readline


def solution(n, c, house):
    house.sort()  # 이진탐색 해야하므로
    # 집들간의 간격의 범위
    start = 1
    end = house[-1]-house[0]
    result = 0
    while(start <= end):
        mid = (start+end)//2  # 가장 인접한 공유기 사이의 거리
        first = house[0]  # 가장 첫집의 위치
        cnt = 1  # 설치 가능한 공유기의 수
        # 작은 순서대로 간격 맞춰서 공유기 놓기
        for i in range(1, n):
            # 간격보다 크게 설치 가능한 경우
            if house[i] >= first+mid:
                first = house[i]
                cnt += 1
        # 공유기가 c개 이상 설치 가능한 경우
        if cnt >= c:
            start = mid+1  # 간격 더 넓히기
            result = mid
        else:
            end = mid-1  # 간격 더 좁혀서 확인해보기
    return result


n, c = map(int, input().split())
house = []  # 집의 위치
for i in range(n):
    house.append(int(input()))
print(solution(n, c, house))
