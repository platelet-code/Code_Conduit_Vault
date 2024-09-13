class ChainedHashTable:
    def __init__(self, capacity: int = 1000003):
        self.capacity = capacity
        self.bucket_heads = [-1] * capacity  # 每个桶的链表头
        self.values = []  # 存储实际的值
        self.next_pointers = []  # 存储链表中下一个元素的索引
        self.size = 0  # 当前哈希表中的元素数量

    def _hash(self, key: int) -> int:
        return (key % self.capacity + self.capacity) % self.capacity

    def insert(self, key: int) -> None:
        bucket = self._hash(key)
        current = self.bucket_heads[bucket]
        while current != -1:
            if self.values[current] == key:
                return  # 键已存在，无需插入
            current = self.next_pointers[current]
        
        self.values.append(key)
        self.next_pointers.append(self.bucket_heads[bucket])
        self.bucket_heads[bucket] = self.size
        self.size += 1

    def query(self, key: int) -> bool:
        bucket = self._hash(key)
        current = self.bucket_heads[bucket]
        while current != -1:
            if self.values[current] == key:
                return True
            current = self.next_pointers[current]
        return False
