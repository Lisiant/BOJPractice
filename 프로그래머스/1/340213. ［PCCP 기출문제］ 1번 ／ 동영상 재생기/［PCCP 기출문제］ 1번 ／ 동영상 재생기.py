def min_to_sec(time):
    m, sec = map(int, time.split(":"))
    return m * 60 + sec

def sec_to_min(time):
    m = str(time // 60)
    sec = str(time % 60)
    
    if len(m) == 1:
        m = '0'+ m
    if len(sec) == 1:
        sec = '0'+ sec

    return  ":".join([m, sec])


    
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = min_to_sec(video_len)
    pos = min_to_sec(pos)
    op_start = min_to_sec(op_start)
    op_end = min_to_sec(op_end)

    for cmd in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        
        if cmd == "next":
            
            if video_len - pos < 10:
                pos = video_len
            else:
                pos += 10
            
        elif cmd == "prev":            
            if pos < 10:
                pos = 0
            else:
                pos -= 10
                
        if op_start <= pos <= op_end:
            pos = op_end

            
    
            
    answer = sec_to_min(pos)            
    return answer