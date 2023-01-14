import sys


def merge_sort(a):  # 정렬

    def merge(a, left, right):  # 병합
        if left < right:
            center = (left + right) // 2

            merge(a, left, center)  # 배열의 앞부분을 병합 정렬
            merge(a, center + 1, right)  # 배열의 뒷부분을 병합 정렬

            j = p = 0   # buff를 탐색하는 인덱스
            k = i = left  # a를 탐색하는 인덱스

            while i <= center:
                buff[p] = a[i]   # a의 앞부분을 buff에 복사
                p += 1
                i += 1

            while i <= right and j < p:  # buff와 a의 뒷부분을 비교
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:  # buff의 나머지 부분을 a에 복사
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n   # 작업용 배열 buff 를 생성
    merge(a, 0, n-1)    # 배열 전체를 병합 정렬
    del buff            # 작업용 배열 소멸
    return a


n = int(input())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

merge_sort(data)

for item in data:
    print(item)
