def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)
    row, col = len(park), len(park[0])
    
    for n in mats:
        if iterate(mats, park, row, col, n):
            answer = max(answer, n)
        
    return answer


def iterate(mats, park, row, col, n):
    
    for i in range(row-n+1):
        for j in range(col-n+1):
            flag = True
            for k in range(n):
                for l in range(n):
                    if park[i+k][j+l] != '-1':
                        flag = False
                        break
                if not flag:
                    break
                    
                    
            if flag:
                return True
        
    return False    
                        
            


