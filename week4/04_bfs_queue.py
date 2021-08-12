# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}
# DFS와 비슷하다 그냥 스택을 쓰냐 큐를 쓰냐의 차이다.
# 1. 시작 노드를 큐에 넣습니다
# 2. 현재 큐의 노드를 빼서 visited 에 추가합니다
# 3. 현재 방문한 노드와 인접한 노드 중에서 방문하지 않은 노드를 스택에 추가한다.

def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue[0]
        # current_node = queue.pop(0) 이렇게 뽑아와도 된다.
        del queue[0:1]
        visited.append(current_node)
        for value in adj_graph[current_node]:
            if value not in visited:
                queue.append(value)

    return visited

print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!