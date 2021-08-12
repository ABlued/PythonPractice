input = 20

# Fibo(N) = Fibo(N - 1) + Fibo(N - 2)
# Fibo(1) = Fibo(2) = 1
def fibo_recursion(n):

    if n == 1 or n == 2: return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765

# 입력값이 클수록 연산량이 많아져서 속도가 너무 느려짐
# 똑같은 연산을 여러 번 하기 때문에 비효율적임