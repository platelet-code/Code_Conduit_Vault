class MinHeap:
    def __init__(self, capacity: int = 10**6+10):
        self.heap = [0] * (capacity + 1)
        self.size = 0

    def up(self, index: int) -> None:
        while index > 1 and self.heap[index] < self.heap[index // 2]:
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index //= 2

    def insert(self, val: int) -> None:
        self.size += 1
        self.heap[self.size] = val
        self.up(self.size)

    def down(self, index: int) -> None:
        child = index * 2
        while child <= self.size:
            if child < self.size and self.heap[child] > self.heap[child + 1]:
                child += 1
            if self.heap[child] < self.heap[index]:
                self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
                index = child
                child = index * 2
            else:
                break

    def extract_min(self) -> Optional[int]:
        if self.size == 0:
            return None
        min_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.down(1)
        return min_val

    def remove(self, index: int) -> None:
        if index <= self.size:
            self.heap[index] = self.heap[self.size]
            self.size -= 1
            self.up(index)
            self.down(index)
