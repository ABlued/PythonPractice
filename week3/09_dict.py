class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        self.items[hash(key) % len(self.items)] = value


    def get(self, key):
        return self.items[hash(key) % len(self.items)]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))

# 이 Dict의 단점은 hash함수로 통해 같은 index 값을 갖는 값이 나오는 충돌이 발생된다.