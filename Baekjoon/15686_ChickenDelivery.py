"""
No. 15686 치킨 배달 
- solution
조합 사용!

"""
from itertools import combinations
#list(permutations(list명,m))
def chickenRoad(comblist,house,chicken):
    citysum=0
    # 도시의 치킨거리 구함 
    for h in house:
        # 집과 해당 치킨집의 거리를 구함 
        mini=1e9
        for c in comblist:
            distance=abs(h[0]-chicken[c][0])+abs(h[1]-chicken[c][1])
            mini=min(mini,distance) # 1가정에 대한 치킨집 거리 
        citysum+=mini
    return citysum
    

def solution(n,m,cityinfo):
    chicken=[]
    house=[]
    for i in range(n):
        for j in range(n):
            if cityinfo[i][j]==1:
                house.append((i,j))
            elif cityinfo[i][j]==2:
                chicken.append((i,j))
    chino=[i for i in range(len(chicken))]
    # 치킨 집 중 m개 선택하는 조합 생성
    choose=list(combinations(chino,m))

    # 조합별로 도시의 치킨거리 구하기 
    minid=1e9
    for k in range(len(choose)):
        citysum= chickenRoad(choose[k],house,chicken)
        minid=min(citysum,minid)
    return minid


n,m=map(int,input().split())
cityinfo=[list(map(int,input().split())) for _ in range(n)]
print(solution(n,m,cityinfo))