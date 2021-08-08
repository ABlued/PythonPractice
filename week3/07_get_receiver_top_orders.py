top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    result = [0]
    for index in range(1, len(heights)):
        stack = heights[:index]

        while len(stack) != 0 :
            if heights[index] < stack.pop() :
                result.append(len(stack) + 1)
                break

        if len(stack) == 0 : result.append(0)

    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!