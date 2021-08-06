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


def get_linked_list_sum(linked_list_1, linked_list_2):
    cur = linked_list_1.head
    sum1 = ''
    sum2 = ''
    while cur is not None:
        sum1  += str(cur.data)
        cur = cur.next

    cur = linked_list_2.head
    while cur is not None:
        sum2 += str(cur.data)
        cur = cur.next
    sum = 0
    return int(sum1) + int(sum2)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))