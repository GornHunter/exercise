__author__ = 'Nancy'


class BST(object):
    def __init__(self, value=None, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def print_helper(self, parentpath):
        a = parentpath[:]
        a.append(self.value)
        if self.right:
            self.right.print_helper(a)
        if self.left:
            self.left.print_helper(a)
        else:
            if self.right is None and self.left is None:
                print(a)


    def print_all_path(self):
        self.print_helper([])

    def mark_big(self):

        if self.left:
            lh = self.left.tree_high()
        else:
            lh = 0

        if self.right:
            rh = self.right.tree_high()
        else:
            rh = 0

        if lh > rh:
            self.big = self.left
        else:
            self.big = self.right

        if self.big:
            self.big.mark_big()


    def print_longest_path(self):
        self.mark_big()

        big = self.big

        while big:
            print(big.value, '-->', end='')
            big = big.big

    def delete(self, value):
        if value == self.value:
            if self.left and self.right:
                me = self.left
                while me.right:
                    me = me.right

                self.value = me.value
                me.delete(me.value)
            elif self.right:
                self.parent.right = self.right
                self.right.parent = self.parent
            elif self.left:
                self.parent.left = self.left
                self.left.parent = self.parent
            else:
                self.parent.left = None
                self.parent.right = None
                # if self.parent.left:
        else:
            if self.value > value and self.left:
                self.left.delete(value)
            else:
                if self.value < value and self.right:
                    self.right.delete(value)


    def nodecount(self):
        if self.left:
            m = self.left.nodecount()
        else:
            m = 0
        if self.right:
            n = self.right.nodecount()
        else:
            n = 0
        return m + n + 1

    def insert(self, value):
        # print("self", self.value, 'value', value)
        if self.value is None:
            self.value = value
            return

        if self.value > value:
            if self.left is None:
                self.left = BST(value, self)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value, self)
            else:
                self.right.insert(value)

    def tree_high(self):
        if self.left:
            m = self.left.tree_high()
        else:
            m = 0

        if self.right:
            n = self.right.tree_high()
        else:
            n = 0
        if m >= n:
            return m + 1
        else:
            return n + 1


    def in_order_print(self):
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()


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


def main():
    bst = BST()
    for i in range(1, 10):
        # print('-------------------, insert', i)
        bst.insert(i)

    for i in range(1, 10):
        if bst.find(i) is None:
            print('error, %s not found' % i)

    bst = BST()
    for i in [3, 5, 1, 4, 8, 0, 11, 16, 9, 10]:
        bst.insert(i)

        # bst.in_order_print()

    # print(bst.delete(11), '$$$$$$$$$$$$$$$$$$$$$$$$')
    # bst.in_order_print()

    # print(bst.print_helper())
    # print(bst.nodecount(), '####################')
    # print('-----------')
    # print(bst.tree_high(), '!!!!!!!!!!!!!!!!!!!!!')
    l = [2, 4, 6, 9, 1, 10, 3, 8, 6, 7]

    bst.print_helper([])


if __name__ == '__main__':

    main()

    arr = list(range(10))
    t = arr[:]
    t.append(11)
    t[1] = 3
    print(arr)
    print(t)
