"""
[ 이코테 - 두 배열의 원소 교체 ]
- Solution
A의 원소 중 가장 큰 수 & B의 가장 작은 원소 바꾸기 
 
"""
def solution(n, k, a, b):
    a.sort()  # 오름 차순 정렬
    b.sort(reverse=True)  # 내림차순 정렬
    for i in range(k):
        # a의 원소가 더 작은 경우에만 교환
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    return sum(a)


n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(n, k, A, B))
