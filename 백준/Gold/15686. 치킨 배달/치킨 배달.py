import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e9)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
shops = []
houses = []
len_shop = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            shops.append([i, j])
            len_shop += 1
        elif graph[i][j] == 1:
            houses.append([i, j])

is_shop_used = [False] * len_shop
temp_shop = [[]] * len_shop
shop_combinations = []


def generate_shop_comb(k, idx):
    if k == m:
        shop_combinations.append(temp_shop[:m])
        return

    for i in range(idx, len_shop):
        if not is_shop_used[i]:
            is_shop_used[i] = True
            temp_shop[k] = shops[i]
            generate_shop_comb(k + 1, i + 1)
            is_shop_used[i] = False


def calc_distance(home, shop):
    return abs(home[0] - shop[0]) + abs(home[1] - shop[1])


def solve():
    res= INF
    
    for comb in shop_combinations:
        sum_house_dist = 0
        
        for house in houses:
            min_dist = INF
            for shop in comb:
                min_dist = min(calc_distance(house, shop), min_dist)
            
            sum_house_dist += min_dist
        res = min(res, sum_house_dist)    
    
    return res
          

generate_shop_comb(0, 0)
print(solve())
