input = [3,2,1,5,9,7,4]


def find_max_plus_or_multiply(array):
    value = input[0]

    for i in range(1, len(input)):
        sum = value + input[i]
        mul = value * input[i]
        if mul < sum : value += input[i]
        elif sum < mul : value *= input[i]
        else : value += input[i]

    return value


result = find_max_plus_or_multiply(input)
print(result)