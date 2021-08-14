input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    stack = []
    result = len(string)
    for split_size in range(1, n//2 + 1):
        splited = [
            string[i:i + split_size]for i in range(0,n,split_size)
        ]
        compression_string = ''
        stack.append(splited[0])
        for i in range(1, len(splited)):
            if stack[len(stack) - 1] != splited[i] :
                count = '' if len(stack) == 1 else len(stack)
                compression_string = compression_string + str(count) + str(stack.pop())
                stack.clear()
                stack.append(splited[i])
            else :
                stack.append(splited[i])

        if len(stack) != 0 :
            count = '' if len(stack) == 1 else len(stack)
            compression_string = compression_string + str(count) + str(stack.pop())
            stack.clear()

        result = min(result, len(compression_string))
        print(splited)
        print(compression_string)
        print(result)

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print(input.split(" "))
print(input)
