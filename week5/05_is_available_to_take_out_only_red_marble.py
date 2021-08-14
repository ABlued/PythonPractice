# from collections import deque
#
# game_map = [
#     ["#", "#", "#", "#", "#"],
#     ["#", "R", ".", "B", "#"],
#     ["#", ".", "#", ".", "#"],
#     ["#", ".", "O", ".", "#"],
#     ["#", "#", "#", "#", "#"],
# ]
# # 동 서 북 남
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# red_ball_location = []
# blue_ball_location = []
# def display(red_ball_location, blue_ball_location):
#     for i in range(len(game_map)):
#         for j in range(len(game_map[i])):
#             if red_ball_location[0] == i and red_ball_location[1] == j :
#                 print('R', end='')
#             elif blue_ball_location[0] == i and blue_ball_location[1] == j:
#                 print('B', end='')
#             else :
#                 print(game_map[i][j],end='')
#         print()
#
#     print()
#
# def move(red_ball_location, blue_ball_location, direction):
#
#     Ry, Rx = red_ball_location
#     By, Bx = blue_ball_location
#     newRX, newRX, newBX, newBY = 0,0,0,0
#     answer = 0
#
#     while True:
#         newRX = Rx + dx[direction]
#         newRY = Ry + dy[direction]
#         newBX = Bx + dx[direction]
#         newBY = By + dy[direction]
#         if  game_map[newRY][newRX] == 'O' and game_map[newBY][newBX] == 'O' :
#             answer = -1
#             break
#         elif game_map[newRY][newRX] != '.' and game_map[newBY][newBX] != '.' : break
#
#         elif game_map[newRY][newRX] == 'O':
#             answer = 1
#             break
#         elif game_map[newBY][newBX] == 'O':
#             answer = -1
#             break
#
#         if game_map[newRY][newRX] != '#' and game_map[newRY][newRX] != 'B':
#             Rx = newRX
#             Ry = newRY
#         if game_map[newBY][newBX] != '#' and game_map[newBY][newBX] != 'R':
#             Bx = newBX
#             By = newBY
#
#
#     red_ball_location = [Ry, Rx]
#     blue_ball_location = [By, Bx]
#     return red_ball_location, blue_ball_location, answer
#
#
#
#     return red_ball_location, blue_ball_location, answer
#
# def is_available_to_take_out_only_red_marble(game_map):
#     red_queue = deque()
#     blue_queue = deque()
#     for i in range(len(game_map)):
#         for j in range(len(game_map[i])):
#             if game_map[i][j] == 'R':
#                 red_ball_location = [i,j]
#             elif game_map[i][j] == 'B':
#                 blue_ball_location = [i,j]
#
#
#     red_queue.append(red_ball_location)
#     blue_queue.append(blue_ball_location)
#
#     answer = False
#     count = 0
#     while count <= 10:
#
#         for i in range(0, len(red_queue)):
#
#             red_ball_location, blue_ball_location, answer = move(red_queue[i], blue_queue[i], 0)
#             if answer == 1 :
#                 break
#             elif answer == 0 :
#                 red_queue.append(red_ball_location)
#                 blue_queue.append(blue_ball_location)
#             display(red_ball_location, blue_ball_location)
#
#             red_ball_location, blue_ball_location, answer = move(red_queue[i], blue_queue[i], 1)
#             if answer == 1:
#                 break
#             elif answer == 0:
#                 red_queue.append(red_ball_location)
#                 blue_queue.append(blue_ball_location)
#             display(red_ball_location, blue_ball_location)
#
#             red_ball_location, blue_ball_location, answer = move(red_queue[i], blue_queue[i], 2)
#             if answer == 1:
#                 break
#             elif answer == 0:
#                 red_queue.append(red_ball_location)
#                 blue_queue.append(blue_ball_location)
#             display(red_ball_location, blue_ball_location)
#
#             red_ball_location, blue_ball_location, answer = move(red_queue[i], blue_queue[i], 3)
#             if answer == 1:
#                 break
#             elif answer == 0:
#                 red_queue.append(red_ball_location)
#                 blue_queue.append(blue_ball_location)
#             display(red_ball_location, blue_ball_location)
#             red_queue.popleft()
#             blue_queue.popleft()
#
#         count += 1
#         if answer == 1: break
#
#     if count <= 10 : return True
#     else: return False
#
#
# print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다


from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
    return r,c, move_count

def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    queue = deque()

    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j


    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break
        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)
            # 파란 공이 먼저 들어간 경우는 무시한다.
            if game_map[next_blue_row][next_blue_col] == 'O':
                continue
            if game_map[next_red_row][next_red_col] == 'O':
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            # visited에 있는 거라면 큐에 집어넣지 않는다
            if not visited[next_red_row][next_red_col][next_blue_col][next_blue_row] :
                visited[next_red_row][next_red_col][next_blue_col][next_blue_row] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, b_count + 1))

    return False

print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
