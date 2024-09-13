class LinkedList:
    def __init__(self, max_size=10**6+5) -> None:
        self.values = [0] * max_size  # 存储节点的值
        self.next_pointers = [-1] * max_size  # 存储下一个节点的索引
        self.head = -1  # 头节点索引
        self.next_available = 0  # 下一个可用的节点索引

    def insert_at_head(self, value: int) -> None:
        self.values[self.next_available] = value
        self.next_pointers[self.next_available] = self.head
        self.head = self.next_available
        self.next_available += 1

    def remove(self, position: int) -> None:
        if position == 0:
            self.head = self.next_pointers[self.head]
        else:
            self.next_pointers[position-1] = self.next_pointers[self.next_pointers[position-1]]

    def insert(self, position: int, value: int) -> None:
        self.values[self.next_available] = value
        self.next_pointers[self.next_available] = self.next_pointers[position-1]
        self.next_pointers[position-1] = self.next_available
        self.next_available += 1

    def print_list(self) -> None:
        current = self.head
        while current != -1:
            print(self.values[current], end=' ')
            current = self.next_pointers[current]
        print()
