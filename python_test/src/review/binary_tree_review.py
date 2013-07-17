__author__ = 'nancy'


class BST(object):
    def __init__(self, value=None, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, value):
        if self.value is None:
            self.value = value
            return
        if self.value > value:
            if self.left is None:
                self.left = BST(value, self)
            else:
                self.left.insert(value)
        if self.value < value:
            if self.right is None:
                self.right = BST(value, self)
            else:
                self.right.insert(value)

    def order_print(self):
        if self.left:
            self.left.order_print()
        print self.value,
        if self.right:
            self.right.order_print()

    def height(self):
        if self.left is None:
            m = 0
        else:
            m = self.left.height()
        if self.right is None:
            n = 0
        else:
            n = self.right.height()
        if m >= n:
            return m + 1
        else:
            return n + 1

    def node_count(self):
        if self.left:
            m = self.left.node_count()
        else:
            m = 0
        if self.right:
            n = self.right.node_count()
        else:
            n = 0
        return m + n + 1

    def find(self, value):
        if self.value == value:
            return self.value
        if self.value > value:
            if self.left:
                return self.left.find(value)
            else:
                return None
        if self.value < value:
            if self.right:
                return self.right.find(value)
            else:
                return None
        else:
            return None

    def delete(self):
        pass

    def find_min(self):
        min = self
        while min.left:
            min = min.left
        return min

    def replace_node_in_parent(self, value):
        if self.parent:
            if self.parent.left == self:
                self.parent.left = value
            if self.parent.right == self:
                self.parent.right = value
        if value:
            value.parent = self.parent

    def __str__(self):
        return "value: %s, left: <%s>, right: <%s>" % (self.value, self.left, self.right)

    def binary_tree_delete(self, value):
        if self.value > value:
            self.left.binary_tree_delete(value)
        elif self.value < value:
            self.right.binary_tree_delete(value)
        else:
            print self
            if self.left and self.right:
                successor = self.right.find_min()
                print 'successor', successor.value
                self.value = successor.value
                successor.binary_tree_delete(successor.value)
            elif self.left:
                self.replace_node_in_parent(self.left)
            elif self.right:
                self.replace_node_in_parent(self.right)
            else:
                self.replace_node_in_parent(None)





def main():
    bst = BST()
    for i in [6, 2, 10, 7, 9, 21, 15, 4, 8, 19, 12]:
        bst.insert(i)

    # bst.order_print()
    # print(bst.height())
    # print(bst.node_count())
    # print(bst.find(18))
    print(bst.find_min(), bst.find_min().value)
    bst.order_print()
    print '\n'
    print bst.node_count(), 'before------------'

    bst.binary_tree_delete(9)
    bst.order_print()
    print '\n'
    print bst.node_count(), 'after---------------'



#describe dictionary and list
# b = [6, 2, 10, 7, 9, 21, 15, 4, 8, 19, 12]
#
# d = dict([(item, "str-%s" % item) for item in b])
#
# print d
#
#
# def cmp(a):
#     return a
#
# b = sorted(b, key=cmp, reverse=True)
# print b


if __name__ == '__main__':
    main()


