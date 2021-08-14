# from collections import deque
#
# c = 17
# b = 3
#
# def findCount(brownLocation, count):
#
#     for i in range(0, 3**count):
#         temp = brownLocation.popleft()
#         brownLocation.append(temp * 2)
#         brownLocation.append(temp - 1)
#         brownLocation.append(temp + 1)
#
#     return brownLocation
#
# def catch_me(cony_loc, brown_loc):
#
#     conyLocation = cony_loc
#     brownLocation = deque()
#     brownLocation.append(brown_loc)
#     cony_speed = 1
#     count = 0
#     # print(conyLocation, brownLocation)
#
#     while conyLocation not in brownLocation :
#         conyLocation = conyLocation + cony_speed
#         if 200000 < conyLocation: break
#         brownLocation = findCount(brownLocation, count)
#         count += 1
#         # print(conyLocation, brownLocation)
#         cony_speed += 1
#
#     return count
#
#
# print(catch_me(c, b))  # 5가 나와야 합니다!


from collections import deque
c = 2
b = 2054
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0)) # 위치와 시간을 담아줄게요!.
    visited = [{} for _ in range(200001)]

    while cony_loc < 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)): # Q. Queue 인데 while 을 안 쓰는 이유를 고민해보세요!
            current_position, current_time = queue.popleft()
            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        time += 1

print(catch_me(c, b))