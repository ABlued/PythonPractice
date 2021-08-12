seat_count = 9
vip_seat_array = [4, 7]
number_of_cases_where_a_person_can_sit = {
    1:1,
    2:2,
    3:3,
    4:5,
    5:8,
    6:13,
    7:21,
    8:34,
}
def Fibo(n):
    if n in number_of_cases_where_a_person_can_sit:
        return number_of_cases_where_a_person_can_sit[n]
    if len(list(filter(lambda k : k in number_of_cases_where_a_person_can_sit.keys(), [n - 1, n - 2]))) > 1:
        number_of_cases_where_a_person_can_sit[n] = number_of_cases_where_a_person_can_sit[n - 1] + number_of_cases_where_a_person_can_sit[n - 2]
    return Fibo(n - 1) + Fibo(n - 2)

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):

    array = []
    result = 1
    count = 0
    for i in range (total_count):
        array.append(i + 1)

    while array:
        if array.pop(0) in fixed_seat_array:
            result *= Fibo(count)
            count = 0
        else :
            count += 1
    if count != 0:
        result *= Fibo(count)

    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
