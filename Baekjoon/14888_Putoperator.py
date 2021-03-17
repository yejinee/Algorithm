"""




"""
maxi=-1e9
mini=1e9

def dfs(value,i,plus,minus,mul,div):
    global maxi,mini,a
    if i==n: #계산 끝나면 min,max update해줄것
        maxi=max(maxi,value)
        mini=min(mini,value)

    else:
        if plus>0: 
            dfs(value+a[i],i+1,plus-1,minus,mul,div)
        if minus>0:
            dfs(value-a[i],i+1,plus,minus-1,mul,div)
        if mul>0:
            dfs(value*a[i],i+1,plus,minus,mul-1,div)
        if div>0:
            dfs(int(value/a[i]),i+1,plus,minus,mul,div-1)

n=int(input())
a=list(map(int,input().split()))
plus,minus,mul,div=map(int,input().split())
dfs(a[0],1,plus,minus,mul,div)
print(maxi)
print(mini)

