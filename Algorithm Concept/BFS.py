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

# BFS
def BFS(graph,root):
    visit=[] # 방문한 Node모음 
    queue=[]
    queue.append(root) # Root Node를 Queue에 넣어주기 

    while queue:
        node=queue.pop(0) # 제일 처음 값 꺼내기 
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node]) # 해당 Node와 연결된 Node들을 Queue에 추가
    return visit

print(BFS(graph,'A'))