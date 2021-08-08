input = [4, 6, 2, 9, 1, 5]


def insertion_sort(array):
    # 제가 구현한 부분
    # result = [array[0]]
    # for i in range(1, len(array)):
    #     for j in range (len(result)) :
    #         if array[i] < result[j] :
    #             result.insert(j, array[i])
    #             break
    #     if len(result) != i + 1 : result.insert(len(result), array[i])
    # return result
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j] :
                array[i - j - 1] , array[i - j] = array[i - j], array[i - j - 1]
            else : break
    return array

input = insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!