input = "가나다라나가"


def is_palindrome(string, i):
    # 내가 푼 로직
    # n = len(string)
    # if i == len(string)//2 : return True
    # if string[i] != string[n - 1 - i]:
    #     return False
    #
    # return is_palindrome(input, i + 1)

    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

# print(is_palindrome(input, 0))
print(is_palindrome(input))