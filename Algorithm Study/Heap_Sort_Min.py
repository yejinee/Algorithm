"""
Heap 라이브러리 이용한 Heap Sort
"""
import heapq

# Min Heap 사용해 오름차순 Heap Sort
def minheapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# Max Heap 사용해 내림차순 Heap Sort
def maxheapsort(iterable):
    h = []
    result = []
    # 음수 형태로 원소를 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


ex = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(minheapsort(ex))
print(maxheapsort(ex))
