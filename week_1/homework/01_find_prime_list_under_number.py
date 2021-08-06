input = 50


# def find_prime_list_under_number(number):
#     isPrime = [True] * (number + 1)
#     isPrime[0] = False
#     isPrime[1] = False
#     i = 2
#     while i*i <= number :
#         if isPrime[i] == True :
#             j = i + i
#             while j <= number :
#                 isPrime[j] = False
#                 j += i
#         i += 1
#     result = []
#     for index  in range(len(isPrime)):
#         if isPrime[index] == True :
#             result.append(index)
#     return result
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in range(2, n):
            if n % i == 0:
                break
            else:
                prime_list.append(n)

    return

result = find_prime_list_under_number(input)
print(result)