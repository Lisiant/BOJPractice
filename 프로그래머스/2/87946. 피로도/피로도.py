def solution(k, dungeons):
    global answer
    answer = 0
    
    vis = [0] * len(dungeons)
    dfs(k, 0, dungeons, vis)
    return answer


def dfs(k, cnt, dungeons, vis):
    global answer
    answer = max(answer, cnt)
    max_cnt = len(dungeons)

    for i in range(max_cnt):
        if vis[i] == 0 and dungeons[i][0] <= k:
            vis[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons, vis)
            vis[i] = 0
