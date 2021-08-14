from collections import deque

# balanced_parentheses_string = "(()))(()"
#
#
# def get_correct_parentheses(balanced_parentheses_string):
#     stack = []
#     number_of_head = number_of_tail = 0
#     result = ''
#     for char in balanced_parentheses_string:
#
#
#         if char == "(":
#             stack.append('(')
#             number_of_head += 1
#         else :
#             stack.append(')')
#             number_of_tail += 1
#
#         if number_of_head != 0 and number_of_head == number_of_tail :
#             checkStack = []
#             temp = stack[1:len(stack) - 1]
#             head = tail = 0
#
#             for i in range(0, len(temp)):
#                 if temp[i] == '(':
#                     checkStack.append(temp[i])
#                     head += 1
#                 else :
#                     checkStack.append(temp[i])
#                     tail += 1
#                 if head < tail :
#                     temp.reverse()
#                     temp = "".join(temp)
#                     temp = "(" + temp + ")"
#                     result += temp
#                     stack.clear()
#                     break
#
#             if stack :
#                 temp = "".join(temp)
#                 temp = "(" + temp +")"
#                 result += temp
#                 stack.clear()
#
#             number_of_head = number_of_tail = 0
#     return result
#
#
# print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!


from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parenthesis(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0
def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string
def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = ''.join(list(queue))
    return u, v
def change_to_correct_parenthesis(string):
# 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if string == "":
        return ""
# 2. 문자열 w를 두 '균형잡힌 괄호 문자열' u,v로 분리한다
# 단 u는 '균형잡힌 괄호 문자열' 로 더 이상 분리할 수 없어야 하며,
# v는 빈 문자열이 될 수 있다.
# () 개수 가 같아야한다.
    u, v = separate_to_u_v(string)

# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해
# 1단계부터 다시 수행한다.
# 3-1. 수행한 결과 문자열을 u에 이어붙인뒤 반환합니다.
# -> change_to_correct_parenthesis
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
# 4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행한다.
# 4-1. 빈 문자열에 첫 번째 문자로 (를 붙인다.
# 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
# 4-3. ')'를 다시 붙인다.
# 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
# 4-5. 생성된 문자열을 반환한다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])




def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis((balanced_parentheses_string)):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
