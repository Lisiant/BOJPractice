def calc_time(diffs, times, limit, level, cnt):
    time_sum = times[0]
    
    for i in range(1, cnt):
        if diffs[i] <= level:
            time_sum += times[i]
        else:
            time_sum += (times[i-1] + times[i]) * (diffs[i] - level) + times[i]
    
        if time_sum > limit:
            return -1
        
    return level

def search_level(max_level, diffs, times, limit, cnt):
    st = 1
    en = max_level
        
    while st <= en:
        
        mid = (st + en) // 2
        
        cur_level = calc_time(diffs, times, limit, mid, cnt)
        
        if cur_level == -1:
            st = mid + 1
        else:
            en = mid - 1
    if cur_level == -1:
        return mid + 1
    
    return mid
    
    
def solution(diffs, times, limit):
    answer = 0
    cnt = len(diffs)
    max_level = max(diffs)
    mid = (1 + max_level) // 2
    
    answer = search_level(max_level, diffs, times, limit, cnt)
    return answer
        
        
    
    