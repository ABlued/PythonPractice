input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:   # array의 길이만큼 아래의 연산이 실행
        if number == element:   #비교 연산 1번 실행
            return True     # 시간복잡도 : N * 1 = N

    return False

result = is_number_exist(7, input)
print(result)