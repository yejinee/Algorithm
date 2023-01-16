from collections import defaultdict

def solution(line):
    alpha_dict = defaultdict(list)    
    max_len = 0
    min_len = 1e9

    # 문자열에서 K개 이상 존재하는 알파벳만 dictionary에 위치 저장
    for i in range(len(line)):
        if line.count(line[i]) >= K:
            alpha_dict[line[i]].append(i)
    
    # K개 이상 존재하는 알파벳이 없는 경우
    if not alpha_dict:
        return (-1,)

    # 해당문자를 K개 포함하는 문자열 길이를 구하기
    for idx_list in alpha_dict.values():
        for j in range(len(idx_list)-K+1):
            alpha_len = idx_list[j+K-1] - idx_list[j] + 1
            
            max_len = max(max_len, alpha_len)
            min_len = min(min_len, alpha_len)

    return min_len, max_len           


T = int(input())
for _ in range(T):
    line = input()
    K = int(input())
    print(*solution(line))