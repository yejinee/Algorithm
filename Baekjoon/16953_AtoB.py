"""
1. 2곱하기
2. 1을 오른쪽에 추가 
A가 B보다 커지면 끝 -> dfs
"""
def dfs(number,cnt):
    global mini
    if number>b:
        return
    elif number==b:
        mini=min(mini,cnt)
        return 

    dfs(number*2,cnt+1)
    dfs(int(str(number)+'1'),cnt+1)
    

a,b=map(int,input().split())
mini=1e9
dfs(a,0)
if mini==1e9:
    print(-1)
else: print(mini+1)