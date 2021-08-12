import heapq

ramen_stock = 6
supply_dates = [4, 10, 25]
supply_supplies = [15, 5, 10]
supply_recover_k = 30

# 1. 현재 재고의 상태에 따라 최곳값을 받아야 한다.
# 2, 제일 많은 값을 뽀아내야 한다.

# 1. 데이터를 넣을 때마다 최댓값을 동적으로 변경시키며
# 2. 최솟/최댓 값을 바로 꺼낼 수 있는 구조를 사용하면 좋다.

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []
    while stock <= k :
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_added_date_index])
            last_added_date_index += 1

        answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))