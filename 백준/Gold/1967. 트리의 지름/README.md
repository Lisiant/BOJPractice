# [Gold IV] 트리의 지름 - 1967 

[문제 링크](https://www.acmicpc.net/problem/1967) 

### 성능 요약

메모리: 36780 KB, 시간: 80 ms

### 분류

깊이 우선 탐색, 그래프 이론, 그래프 탐색, 트리

### 제출 일자

2024년 1월 23일 15:01:38

### 문제 설명

<p>트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.</p>

<p><img alt="" height="123" src="https://www.acmicpc.net/JudgeOnline/upload/201007/ttrrtrtr.png" width="310"></p>

<p>이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.</p>

<p>입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.</p>

<p><img alt="" height="152" src="https://www.acmicpc.net/JudgeOnline/upload/201007/tttttt.png" width="312"></p>

<p>트리의 노드는 1부터 n까지 번호가 매겨져 있다.</p>

### 입력 

 <p>파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.</p>

### 출력 

 <p>첫째 줄에 트리의 지름을 출력한다.</p>

# 풀이

### 로직

1. 임의의 노드 x에서 가장 먼 거리에 있는 노드 y를 구한다.
2. 노드 y에서 가장 먼 거리에 있는 노드 z를 구한다.
3. 노드 y와 노드 z를 잇는 경로의 길이가 트리의 지름이다.

### 이유

- 트리에서 두 노드 사이를 잇는 경로는 항상 하나만 존재한다.
- 트리의 지름을 구성하는 두 노드 중 한 노드와 임의의 한 노드는 항상 유일하게 연결되어 있다.
- 임의의 한 노드로부터 트리의 지름을 구성하는 두 노드 중 하나를 찾을 수 있다.
- 그 노드로부터 가장 먼 거리에 있는 노드가 트리의 지름을 구성하는 다른 한 노드이다.  

따라서 아무 노드(루트)에서 가장 먼 가중치를 가진 노드를 구하고, 해당 노드에서 가장 먼 노드까지의 거리를 구하면 된다.

처음에 O(n^2) 방식으로 풀어서 시간 초과가 났었는데, 그 이유는 dfs 함수를 설계를 잘못했기 때문이었다.

**시간초과 코드**

```python
def dfs(st, en, cur):
    vis[st] = True

    if st == en:
        temp[en] = cur
        return cur

    for node, edge in tree[st]:
        if not vis[node]:
            dfs(node, en, cur + edge)

for i in range(1, n + 1):
    vis = [False] * (n + 1)
    dfs(1, i, 0)
```

dfs 함수의 경우 st 노드에서 시작해서 en 노드까지의 거리를 구했고, st == en인 경우 temp 노드에 값을 저장하고 return 하도록 하였다. 

이후 1번부터 n+1번 노드까지 반복적으로 dfs를 진행하면서 1번 노드와의 각 노드의 거리를 측정한다.

방문 처리는 vis 배열로 진행해야 했기 때문에 매 반복마다 초기화를 위해 vis 배열을 새로 선언하였다.

1번 노드에서 각 노드의 거리를 구하고, 가장 거리가 긴 노드를 찾은 후 해당 노드에서 같은 작업을 한번 더 진행한다.

하지만 이는 O(n^2)이므로 시간초과이다. 개선한 코드는 다음과 같다.

**정답 코드**
```python

def dfs(st, cur, vis):
    for node, edge in tree[st]:
        if vis[node] == -1:
            vis[node] = cur + edge
            dfs(node, cur + edge, vis)


dist_from_root = [-1] * (n + 1)
dist_from_root[1] = 0
dfs(1, 0, dist_from_root)

```

O(n) 으로 접근하기 위해 dfs 함수의 구조를 변경하였다.

우선 방문 처리를 가중치를 기록하는 배열을 받아서 처리하였다. vis 배열의 값이 변하지 않은 경우에만 재귀함수로 타고 들어가는 방식을 적용하였다.

종료 조건을 삭제하였다. 처음 dfs 함수를 구현했을 때는 반복문 사용을 염두에 두고 작성하였기 때문에 어쩔 수 없이 종료 조건을 명시하였는데, 잘못된 이해에서 비롯된 비효율성이었다. dfs 함수 내부에서 전체 노드를 한번 순회하기 때문에 시간 복잡도를 낮출 수 있는 방향으로 설계하였다.

`dfs(1, 0, dist_from_root)` 를 실행하고 나면 vis 배열에는 1번 노드부터 각 노드의 거리가 저장된다. 이후 한번 더 dfs를 실행.


