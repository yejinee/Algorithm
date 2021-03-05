"""
[ 이코테 - 정렬된 배열에서 특정 수의 개수 구하기 ]

- solution
Key point! => 특정 수의 시작위치와 끝 위치 찾아 줄 것 

★ bisect lib 이용하기
bisect_left(arr,x): arr에서 x가 있는 제일 앞 idx
bisect_right(arr,x): arr에서 x나열하고 제일 끝 idx

"""
# 배열의 왼쪽, 오른쪽 인덱스 구해주는 lib
from bisect import bisect_left, bisect_right

def solution(x, arr):
    ridx = bisect_right(arr, x)
    lidx = bisect_left(arr, x)
    cnt = ridx-lidx
    if cnt == 0:
        return -1
    else:
        return cnt


n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(x, arr))
