class DoublyLinkedList:
    def __init__(self, max_size=10**5+10) -> None:
        self.max_size = max_size
        self.val = [0] * max_size  # 存储节点的值
        self.left = [0] * max_size  # 左指针
        self.right = [0] * max_size  # 右指针
        self.idx = 2  # 当前可用的节点索引，从2开始
        self.init()

    def init(self) -> None:
        # 0是左端点，1是右端点
        self.right[0] = 1
        self.left[1] = 0

    def insert(self, k: int, x: int) -> None:
        self.val[self.idx] = x
        self.right[self.idx] = self.right[k]
        self.left[self.idx] = k
        self.left[self.right[k]] = self.idx
        self.right[k] = self.idx
        self.idx += 1

    def remove(self, k: int) -> None:
        self.right[self.left[k]] = self.right[k]
        self.left[self.right[k]] = self.left[k]

    def print_list(self) -> None:
        i = self.right[0]
        while i != 1:
            print(self.val[i], end=' ')
            i = self.right[i]
        print()
