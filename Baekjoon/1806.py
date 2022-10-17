import sys
input = sys.stdin.readline

def solution(N,S,num_list):
    ans = 100001
    s = 0
    i,j = 0,0
    while True:
        if s>=S:
           s -= num_list[i]
           ans = min(ans, j-i)
           i+=1

        elif j == N:
            break

        else:
            s += num_list[j]
            j+=1

    ans = 0 if (ans==100001) else ans
    
    return ans


N, S = map(int, input().split())
num_list = list(map(int, input().split()))
print(solution(N,S,num_list))