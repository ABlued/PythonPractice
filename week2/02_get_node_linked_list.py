class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        count = 0;
        cur = self.head
        while count < index :
            cur = cur.next
            count += 1
        return cur.data

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(13)
print(linked_list.get_node(2)) # -> 5를 들고 있는 노드를 반환해야 합니다!