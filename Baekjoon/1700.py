from audioop import mul
from re import L
import sys
input = sys.stdin.readline

def solution(N,K,product_lst):
    ans = 0
    multitap = []
    for idx,product_no in enumerate(product_list):
        # 제품이 이미 꽂혀있는 경우
        if product_no in multitap:
            continue
        # 멀티탭에 자리가 있는 경우
        elif len(multitap)<N:
            multitap.append(product_no)
        # 자리가 꽉차 있는 경우
        else:
            idx_list = []   # 새롭게 꽂아야하는 값들 중 이미 꽂혀있는 값
            for i in range(N): 
                # (1). 이미 꽂혀있는 값들이 다음에 사용되지 않는 경우
                idx_later = product_lst[idx:].index(multitap[i]) # 멀티탭의 값
                idx_list.append(idx_later)
            outidx = idx_list.index(max(idx_list))
            del multitap[outidx]
            multitap.append(product_no)
            ans += 1 


            for multi_value in multitap:
                idx_later = product_list[idx:].index(multi_value) #멀티탭값이 기존의 프로덕트에 또 있는지 체크
                idx_list.append(idx_later)
            out_idx = idx_list.index(max(idx_list))
            del multitap[out_idx]
            multitap.append(product_no)
            ans += 1
            
    return ans

N,K = map(int,input().split())
product_list = map(int,input().split())
