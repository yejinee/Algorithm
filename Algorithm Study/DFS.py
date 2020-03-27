"""
            A
    B                C
D       E       F          G
H     I     J


"""

# 1. GRAPH로 나타내기 - Dictionary 사용
graph={ 'A': ['B','C'],
'B':['A','D','E'],
'C':['A','F','G'],
'D':['B','H', 'I'],
'E':['B','J'],
'F':['C'],
'G':['C'],
'H':['D'],
'I':['D'],
'J':['E']
}

# DFS
def DFS(graph, root):
    visit=[] # 방문한 Node 모음
    stack=[] 
    stack.append(root) # Root Node를 Stack에 넣어주기

    while stack:
        node=stack.pop() # list의 마지막 값 부터 꺼내기
        if node not in visit: #방문했던 Node가 아닌 경우
            visit.append(node) 
            stack.extend(reversed(graph[node])) # 해당 node와 연결된 Node들을 Stack에 추가 
    return visit

print(DFS(graph,'A'))


