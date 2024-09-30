import heapq

def solution(scoville, K):
    answer = 0
    data = []
    for item in scoville:
        heapq.heappush(data, item)
    cur = 0
    cnt = 0
    
    while len(data) >= 2:
        
        if data[0] >= K:
            return cnt
        
        a = heapq.heappop(data)
        b = heapq.heappop(data)
    
        cur = a + b * 2
        cnt += 1 
        heapq.heappush(data, cur)
    
    if len(data) == 1 and data[0] >= K:
        return cnt
    return -1