array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    leftIndex = 0
    rightIndex = 0
    result = []
    while leftIndex != len(array1) and rightIndex != len(array2):
        if array1[leftIndex] < array2[rightIndex] :
            result.append(array1[leftIndex])
            leftIndex += 1
        else :
            result.append((array2[rightIndex]))
            rightIndex += 1

    if leftIndex != len(array1):
        for index in range (leftIndex, len(array1)):
            result.append(array1[index])

    elif rightIndex != len(array2):
        for index in range (rightIndex, len(array2)):
            result.append(array2[index])

    return result

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!