__author__ = 'nancy'


class HashTable(object):
    def __init__(self):
        self.arr = [None] * 100
        self.hash_func = id()

    def set(self, key, value):
        index = self.hash_func(key) % len(self.arr)
        self.arr[index]=(key,value)


    def get(self, key, value):
        pass


def test_hash_test():
    ht = HashTable()
    ht.set(100, 1)
    ht.set(100, 2)
    ht.set(120, 3)

    ht.get(125)
    ht.get(100)


print test_hash_test()