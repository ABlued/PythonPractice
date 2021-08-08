s = "(())(())"


def is_correct_parenthesis(string):
    stack = []
    for v in string:
        if v == '(':
            stack.append('(')
        else :
            if(len(stack) == 0) : return  False
            else : stack.pop()

    if len(stack) == 0 : return True
    return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!