def solution(N, road, city):
    budget = 0
    now = 0
    while now<len(city)-1:
        next = len(city)-1
        # check
        for idx in range(now, len(city)):
            if city[now] > city[idx]:
                next = idx
                break
        # get budget
        for idx in range(now, next):
            budget += (city[now] * road[idx])
        now = next
        
    return budget

             

N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
print(solution(N, road, city))