__author__ = 'nancy'


class HashTable(object):
    def __init__(self):
        self.array = [None] * 5
        self.lane = [None] * 10
        self.hash_func = id

    def get(self, key):
        idx = self.hash_func(key) % len(self.lane)
        while 1:
            item = self.lane[idx % len(self.lane)]
            if item:
                i_key, i_value = item
                if i_key == key:
                    return i_value
                else:
                    idx =(idx+1)%len(self.lane)
            else:
                return None


    def set(self, key, value):
        i = 0
        idx = self.hash_func(key) % len(self.array)
        while 1:
            if self.array[idx] is None:
                self.array[idx] = (key, value)
                return
            else:
                old_key, old_value = self.array[idx]
                if old_key == key:
                    # idx = (idx + 1) % len(self.array)
                    self.array[idx] = (key, value)
                    return
                # TODO resize hash table, reinsert all the exist key & value, then reinsert key&value
                else:
                    idx = (idx + 1) % len(self.array)
                    i += 1
                    if i == 5:
                        # class resize_hash_table(HashTable):
                        # def __init__(self):

                        # def reinsert(self,key,value):
                        #     index=self.hash_func(key)%len(self.lane)

                        for t in self.array:
                            l_key, l_value = t
                            index = self.hash_func(l_key) % len(self.lane)
                            while 1:
                                if self.lane[index] is None:
                                    self.lane[index] = t
                                    break
                                else:
                                    index = (index + 1) % len(self.lane)
                        if self.lane[idx] is None:
                            self.lane[idx] = (key, value)
                            return
                        else:
                            idx = (idx + 1) % len(self.lane)


def test_hash_table():
    ht = HashTable()
    ht.set("100", 1)

    ht.set("130", 2)
    ht.set("110", 4)
    ht.set("105", 5)
    ht.set("118", 2)
    ht.set("120", 3)

    print ht.get("111")
    print ht.get("100")
    print ht.get("120")

print test_hash_table()
