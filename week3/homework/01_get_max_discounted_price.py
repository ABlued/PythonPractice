shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    i = 0
    while  i < len(prices) - 1 :
        prices[i] = prices[i] * ( (100 - coupons[i]) / 100 )
        i += 1

    print(prices)
    return sum(prices)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.