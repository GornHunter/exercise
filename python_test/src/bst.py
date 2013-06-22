__author__ = 'Nancy'


class BST(object):
    def __init__(self, value=None):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, value):
        print("self", self.value, 'value', value)
        if self.value is None:
            self.value = value
            return

        if self.value > value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if self is None:
            return None
        elif self.value == value:
            return value

        if self.value > value:
            if self.left:
                return self.left.find(value)
        else:
            if self.right:
                return self.right.find(value)
        return None

    def delete(self, value):
        if self.value is None:
            return None
        elif self.value > value:
            return self.left.delete(value)
        elif self.value < value:
            return self.right.delete(value)

        # self.value == value

        if self.right and self.left:
            to_delete = self.find_max()
            self.value = to_delete.value
            to_delete.delete(value)
        # elif self.right:
        # elif self.left:
        # else:
        #     self.


    def find_max(self):
        current = self
        while current:
            current = current.right
        return current


def main():
    bst = BST()
    for i in range(1, 10):
        print('-------------------, insert', i)
        bst.insert(i)

    for i in range(1, 10):
        if bst.find(i) is None:
            print('error, %s not found' % i)


if __name__ == '__main__':
    main()
