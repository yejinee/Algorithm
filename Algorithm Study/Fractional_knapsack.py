"""
[ Fractional Knapsack ]

n개의 물건과 1개의 배낭이 있다 
물건 i의 무게는 W(i), 값어치는 P(i), 배낭용량은 M까지 가능 
이윤이 최대가 되도록 물건을 담는 방법? (물건을 잘라서 담을 수 있다)

[ solution ]
- Greedy Algorithm을 사용 

< Fractional Knapsack Function >
1. 무게 당 값어치가 큰 물건순서대로 정렬해준다 -> Sortitem
2. list의 앞에서 차례로 가방에 담을 수 있는 물건들을 담아준다 
   -> 즉, M-item의 무게가 0보다 크면 계속해서 반복 
3. M이 남았다면, 안담은 item의 부분만 담아준다.
    
"""


def Sortitem(iteminfo):
    for i in range(len(iteminfo)):
        iteminfo[i].append(round(iteminfo[i][1]/iteminfo[i][0],2)) # price/weight값을 저장
    iteminfo.sort(key=lambda x:x[2]) # price/weight값이 큰 순서대로 정렬
    iteminfo.reverse()



def Factional_Knapsack(iteminfo,M):
    Sortitem(iteminfo)
    i=0
    price=0
    while (M-iteminfo[i][0])>=0:
        print(i)
        M-=iteminfo[i][0]
        price+=iteminfo[i][1]
        i+=1
        if i>=len(iteminfo): # 모든 item들을 다 담은 경우
            break
    # 남은 경우에 
    if M>0 and i<len(iteminfo):
        price+=iteminfo[i][1]*(round(M/iteminfo[i][0],2))
    return price

    
        
# Data input
itemlist=[]
n=int(input('물건 갯수?'))
M=int(input('배낭 용량? '))
for i in range(n):
    item= list(map(int,input('물건의 무게, 값어치를 차례로 입력').split()))
    itemlist.append(item)


print(Factional_Knapsack(itemlist,M))


