# k = 4  # 말의 개수
#
# chess_map = [
#     [0, 0, 2, 0],
#     [0, 0, 1, 0],
#     [0, 0, 1, 2],
#     [0, 2, 0, 0]
# ]
#
# start_horse_location_and_directions = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 2, 0],
#     [2, 2, 2]
# ]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
# dr = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
#
# def start_horse(horse_count, current_stacked_horse_map, start_horse_location_and_directions):
#     for i in range (0, horse_count):
#         current_stacked_horse_map[start_horse_location_and_directions[i][0] * 4 + start_horse_location_and_directions[i][1]].append(i + 1)
#     return current_stacked_horse_map
#
# def forward(horse_number, current_stacked_horse_map, horse_location_and_directions):
#     index = current_stacked_horse_map[horse_location_and_directions[horse_number][0] * 4 + horse_location_and_directions[horse_number][1]].index(horse_number+1)
#     move_stack = current_stacked_horse_map[horse_location_and_directions[horse_number][0] * 4 + horse_location_and_directions[horse_number][1]][index:]
#     del current_stacked_horse_map[horse_location_and_directions[horse_number][0] * 4 + horse_location_and_directions[horse_number][1]][index:]
#
#     if 0 <= horse_location_and_directions[horse_number][0] + dr[horse_location_and_directions[horse_number][2]] < len(chess_map[0]) and 0 <=  horse_location_and_directions[horse_number][1] + dy[horse_location_and_directions[horse_number][2]] < len(chess_map[0]) :
#
#         for value in move_stack:
#             current_stacked_horse_map[
#                 (horse_location_and_directions[value - 1][0] + dr[horse_location_and_directions[value - 1][2]]) * 4 +
#                 horse_location_and_directions[value - 1][1] + dy[horse_location_and_directions[value - 1][2]]
#             ].append(value)
#             horse_location_and_directions[value - 1][0] += dr[horse_location_and_directions[value - 1][2]]
#             horse_location_and_directions[value - 1][1] += dy[horse_location_and_directions[value - 1][2]]
#     else :
#         for value in move_stack:
#             horse_location_and_directions[value - 1][2] = reverse_dirction(horse_location_and_directions[value - 1][2])
#             current_stacked_horse_map[
#                 (horse_location_and_directions[value - 1][0] + dr[horse_location_and_directions[value - 1][2]]) * 4 +
#                 horse_location_and_directions[value - 1][1] + dy[horse_location_and_directions[value - 1][2]]
#                 ].append(value)
#             horse_location_and_directions[value - 1][0] += dr[horse_location_and_directions[value - 1][2]]
#             horse_location_and_directions[value - 1][1] += dy[horse_location_and_directions[value - 1][2]]
#
#     return current_stacked_horse_map, horse_location_and_directions
#
# def reverse_dirction(direction):
#     if direction == 0:
#         return 1
#     elif direction == 1:
#         return 2
#     elif direction == 2:
#         return 3
#     else :
#         return 4
#
#
#
#
# def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
#     current_stacked_horse_map = [[] * len(game_map)] * len(game_map)**2
#     for i in range (0, len(game_map[0])**2):
#         current_stacked_horse_map[i] = []
#
#     current_stacked_horse_map = start_horse(horse_count, current_stacked_horse_map, horse_location_and_directions)
#     print(current_stacked_horse_map)
#     count = 0
#     while count < 1000:
#         for i in range(0, horse_count):
#             current_stacked_horse_map, horse_location_and_directions = forward(i, current_stacked_horse_map, horse_location_and_directions)
#
#
#
#         count += 1
#
#     return
#
#
# print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다


k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)
    turn_count = 1

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dy[d]
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_r] == 2:
                new_d = get_d_index_when_go_back(d)
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dy[new_d]
                # 가기로 한 곳이 막혀있으면 안감
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_r] == 2:
                    continue

            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count += 1


    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다