class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        aryLen = len(self.items)
        if aryLen < 3 : return
        compareIndex = aryLen - 1

        while 1 < compareIndex:

            if self.items[compareIndex] < self.items[compareIndex // 2]: break
            self.items[compareIndex], self.items[compareIndex // 2] = self.items[compareIndex // 2] , self.items[compareIndex]
            compareIndex = compareIndex // 2



max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!