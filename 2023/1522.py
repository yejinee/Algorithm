def solution(s):
    # 1. 문자열 중 'a'의 갯수 구하기
    a_cnt = 0
    for alphabet in s:
        if alphabet == 'a':
            a_cnt += 1

    # 2. a_cnt만큼 슬라이딩윈도우 수행
    min_cnt = 1e9
    for i in range(len(s)):
        b_cnt = 0
        for j in range(i, i+a_cnt):
            test = s[j%len(s)]
            if s[j%len(s)] == 'b':
                b_cnt += 1
        min_cnt = min(min_cnt, b_cnt)

    return min_cnt

s = input()
print(solution(s))