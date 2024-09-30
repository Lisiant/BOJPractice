from collections import deque
def solution(begin, target, words):
    answer = 0
    

    def check_word(w1, w2):
        cnt = 0
        
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                cnt +=1
        
        if cnt == 1:
            return True
        
        return False
    
    
    def bfs(begin, idx):
        q = deque()    
        q.append((begin, idx))
        
        if target not in words:
            return 0
        
        while q:
            temp, depth = q.popleft()
            if temp == target:
                return depth

            for word in words:
                if check_word(temp, word):
                    q.append((word, depth+1))
        
    
    answer = bfs(begin, 0)    

    return answer