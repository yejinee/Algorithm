"""
[ 1253. 좋다 ]
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

[ INPUT ]
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)


[ OUTPUT ]
좋은 수의 개수를 첫 번째 줄에 출력한다.

"""
import sys
input = sys.stdin.readline

def check_good(find_value_list, find_value):
    """
    list에서 2개값을 더해 value가 만들어지는 지 체크하는 함수
    """
    s_idx, e_idx = 0, len(find_value_list)-1
    while s_idx != e_idx:
        plus_value = find_value_list[s_idx] + find_value_list[e_idx]
        if plus_value == find_value:
            return True
        elif plus_value < find_value:
            s_idx += 1
        else: e_idx -= 1    

    return False


def solution(N, num_list):
    good_cnt = 0
    sort_num_list = sorted(num_list)
    for i in range(len(sort_num_list)):
        find_value_list, find_value = sort_num_list[:i] + sort_num_list[i+1:] , sort_num_list[i]
        if check_good(find_value_list, find_value): good_cnt += 1
    return good_cnt



N =int(input())
num_list = list(map(int,input().split()))

print(solution(N, num_list))