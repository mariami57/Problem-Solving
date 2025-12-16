class MyHashSet:

    def __init__(self):
        self.my_set = []

    def add(self, key: int) -> None:
        if key not in self.my_set:
            self.my_set.append(key)

    def remove(self, key: int) -> None:
        if key in self.my_set:
            self.my_set.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.my_set:
            return True
        else:
            return False

