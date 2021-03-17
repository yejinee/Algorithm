"""
[ 이코테 - 고정점 찾기 ]

"""
def solution(a, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    if a[mid] == mid:
        return mid
    elif a[mid] < mid:  # 오른쪽만 해주면 됌
        start = mid+1
    else: # 왼쪽만 해주면 된다
        end = mid-1
    return solution(a, start, end)


N = int(input())
a = list(map(int, input().split()))
print(solution(a, 0, N-1))
