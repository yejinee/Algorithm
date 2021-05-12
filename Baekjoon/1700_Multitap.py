"""
Q 1700. 멀티탭 스케쥴링
 [ Solution ]
 페이징 기법 중 OPT(최적교체) 활용해 푸는 문제
 
 - 이 문제에 사용하는 이유
 미리 멀티탭에 꽂을 순서가 정해져 있기 때문!

 
 * OPT : 앞으로 일어날 page fault정보를 예측해 앞으로 가장 오랫동안 
 사용하지 않을 페이지를 교체하는 기법 
"""

def solution(n,k,name):
    multitap=[]
    cnt=0
    for i,elec in enumerate(name) :
        # 1. 이미 멀티탭에 꽂혀 있는 경우 
        if elec in multitap:
            continue
        # 2. 멀티탭에 빈 곳이 있는 경우
        elif len(multitap)<n:
            multitap.append(elec)
            continue
        
        # 3. 멀티탭에 빈 공간 없는 경우 
        else:
            idxs=[]
            for j in range(n):
                # 3-1.멀티탭에 꼽힌 것들 중 이후에 사용되는게 없는 경우 -> 사용하지 않는거 뽑기 
                try:
                    idx=name[i:].index(multitap[j])
                 # 3-2. 멀티탭에 꼽힌 것들 중 이후에 사용되는게 있는 경우 
                # -> 가장 나중에 사용하는 전기용품 뽑고 새로운거 꽂기
                except:
                    idx=101
                idxs.append(idx)
            outidx=idxs.index(max(idxs))
            del multitap[outidx]
            multitap.append(elec)
            cnt+=1
    return cnt

n,k=map(int,input().split())
name=list(map(int,input().split()))
print(solution(n, k, name))
       
