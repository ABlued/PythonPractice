input = [4, 6, 2, 9, 1, 3]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    for index in range (len(array)):
        for compareIndex in range (1, len(array) - index):
            if array[compareIndex] < array[compareIndex - 1]:
                array[compareIndex], array[compareIndex - 1] = array[compareIndex - 1], array[compareIndex]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!