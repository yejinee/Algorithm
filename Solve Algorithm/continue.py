# [ 이코테 -특정한 합을 가지는 부분 연속 수열 찾기 ]

def solution(data, m):
    cnt = 0
    end = 0
    total = 0
    # start 증가 
    for start in range(len(data)):
        # end를 계속 증가
        while total < m and end < len(data):
            total += data[end]
            end += 1
        # 부분합이 m일때 
        if total == m:
            cnt += 1
        total -= data[start]

    return cnt


data = [1, 2, 3, 2, 5]
print(solution(data, 5))
