current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
CLEARD = 2
directionX = [0, -1, 0, 1]
directionY = [-1, 0, 1, 0]

def get_d_index_when_rotate_to_left(d):
    if d == 3 : return 0
    else : return d + 1
def append_element(queue, room_map, cur_d, cur_xy):
    for index in range(0, 4):
        cur_d = get_d_index_when_rotate_to_left(cur_d)
        queue.append(room_map[cur_xy[0] + directionY[cur_d]][cur_xy[1] + directionX[cur_d]])
    return queue
def back(cur_xy, cur_d):

    cur_xy = [cur_xy[0] + (- 1 * directionY[cur_d]), cur_xy[1] + (- 1 * directionX[cur_d])]
    return cur_xy

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    room_map[r][c] = CLEARD
    count = 1
    cur_d = get_d_index_when_rotate_to_left(d)
    cur_xy = [r, c]
    queue = []
    queue = append_element(queue, room_map, cur_d, cur_xy)

    while queue :

        if 0 not in queue :
            if queue[1] == 1:
                break
            else :
                cur_xy = back(cur_xy, cur_d)
                queue.clear()
                queue = append_element(queue, room_map, cur_d, cur_xy)
        else :
            for i in range(0,4):
                isCleard = queue.pop(0)
                if isCleard == 1 or isCleard == 2:
                    cur_d = get_d_index_when_rotate_to_left(cur_d)
                else :
                    cur_d = get_d_index_when_rotate_to_left(cur_d)
                    cur_xy = [cur_xy[0]+directionY[cur_d], cur_xy[1]+directionX[cur_d]]
                    room_map[cur_xy[0]][cur_xy[1]] = CLEARD
                    count += 1
                    queue.clear()
                    queue = append_element(queue, room_map, cur_d, cur_xy)
                    break

    return count
# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))