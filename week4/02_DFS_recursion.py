# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

# 1. 루트 노드인 1부터 탐색한다.
# 2. 현재 방문한 노드를 visited_array 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드에 방문합니다.
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # 2.
    if cur_node not in visited : visited.append(cur_node)
    # 3.
    for v in adjacent_graph:
        if v not in visited_array :
            dfs_recursion(adjacent_graph, v, visited_array)

dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!