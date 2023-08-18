import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

result = 0

while start <= end:

    mid = (start+end) // 2

    #total = 0
    # for tree in trees:
    #    if tree > mid:
    #        total += tree - mid

    total = sum(tree-mid for tree in trees if tree >
                mid)  # 리스트 내포와 비슷한 형식, 이게 더 빠름

    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)

'''
못푼 이유:
tree_remain (지금 수정한 코드에서는 total) 값과 m 값을 비교할 때
tree_remain > m / tree_remain < m / else 로 구분할 것이 아니라
tree _remain < m / else 로 구분했어야 함.

즉, 나무의 총 높이가 m과 동일하더라도 m의 높이를 높여보는 것이 바람직하다.
나무의 높이가 m보다 크거나 같을 때 정답이 될 수 있으므로 
각 시행마다 result에 mid 값을 저장해놓아야 한다.

일반적으로 이진 탐색에서는 분기를 작을 때 클 때 같을 때 3가지로 구분해놓은 반면
이 문제에서는 찾고자 하는 값을 찾았을 때에도, 즉 target == data[mid]일 때에도
더 큰값을 찾기 위해 탐색을 계속해야 하므로

target == data[mid]일 때의 조건을 고려할 필요가 없다.

만약 그럼에도 불구하고 3가지 분기로 나누어서 풀고 싶다 하면
아래 코드처럼 하면 된다.


op_lst = list(map(int, sys.stdin.readline().split()))
tree_lst = sorted(list(map(int, sys.stdin.readline().split()))) 
# 주어진 나무들의 높이 리스트

tree_cnt,target_tree_h = op_lst[0],op_lst[1] 
# 나무의 수 / # 집에 가져가려고 하는 나무 길이
tree_max = max(tree_lst) # 나무 중 가장 큰 나무 높이

# 잘라진 나무의 합과 목표 합을 비교
def get_tree_sum(cutter_h):
    tree_sum = 0
    for i in range(tree_cnt-1,-1,-1): # 정렬된 tree list를 내림차순으로 확인
        tree_sub = tree_lst[i]- cutter_h # 나무를 자르고 난 각각의 나머지 길이
        if tree_sub <= 0 : # 음수일 경우 0
            tree_sub = 0
        tree_sum += tree_sub # tree_sum에 저장

        if tree_sum > target_tree_h:  # 목표 나무 길이를 다 채웠으면 break
            break
    return tree_sum

cutter_start = 0
cutter_end = tree_max -1

while True:
    cutter_median = (cutter_start+cutter_end)//2
    sum_by_cutter = get_tree_sum(cutter_median)
    
    if sum_by_cutter == target_tree_h:
        print(cutter_median)
        break
    elif sum_by_cutter > target_tree_h:  # 시작 범위 ~ val로 범위를 좁힌다.
        cutter_start = cutter_median -1

    elif sum_by_cutter < target_tree_h: # val ~ 끝 범위로 범위를 좁힌다.
        cutter_end = cutter_median -1
    
    if cutter_start > cutter_end: # 이 코드에서는 start와 end가 교차하는 일이 없어야 하기 때문에 꼭 필요한 코드는 아님.
        print(cutter_median)
        break

'''
