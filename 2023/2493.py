# stack 이용해서 시간초과 해결
def solution(N, tower):
    ans = []
    stack = []
    for i in range(N):
        while stack:
            before = stack[-1][1] 
            # 수신 가능한 탑 존재하는 경우(존재할때까지 탐색)
            if before > tower[i]:
                ans.append(stack[-1][0]+1)
                break
            # 수신할 탑 없는 경우
            else:
                stack.pop()
        # stack이 비는 경우
        if not stack:
            ans.append(0)
        stack.append([i, tower[i]])
    return ans

# input
N = int(input())
tower = list(map(int, input().split()))


# output
print(*solution(N, tower))