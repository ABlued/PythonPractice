finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # count = len(array)//2
    #
    # while True:
    #     if(count < target): del array[0:len(array)//2]
    #     elif(target < count): del array[len(array)//2:]
    #     else : return count
    #     count = array[len(array)//2]

    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target: return array[current_guess]
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else :
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)