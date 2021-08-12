class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self, length):
        self.items = []
        for i in range(length):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)


    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

menu = LinkedDict(10)
menu.put("apple", 1000)
menu.put("potato", 500)
menu.put("melon", 9000)
menu.put("iceCream", 1500)
menu.get("apple")
menu.get("potato")