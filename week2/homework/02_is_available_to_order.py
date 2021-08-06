shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 떡복이 만두 사이다 오뎅 콜라
def is_available_to_order(menus, orders):
    menus.sort()
    for char in orders:
        tempMenus = menus[:]

        while len(tempMenus) != 0:
            centerIndex = len(tempMenus)//2
            compareChar = tempMenus[centerIndex]
            if char > compareChar : del tempMenus[0:centerIndex + 1]
            elif char < compareChar : del tempMenus[centerIndex:]
            else : break

        if len(tempMenus) == 0 : return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
