class MyHashSet:

    def __init__(self):
        self.listi = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.listi.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.listi.remove(key)
        

    def contains(self, key: int) -> bool:
        for elem in self.listi:
            if elem == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)