class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        if node == None:
            node.value = value
            return
        while True:
            if value < node.value:
                if node.left == None:
                    node.left = BinarySearchTree(value)
                    break
                node = node.left
            elif value > node.value:
                if node.right == None:
                    node.right = BinarySearchTree(value)
                    break
                node = node.right

    def contains(self, target):
        node = self

        while True:
            if node == None:
                return False
            elif node.value == target:
                return True
            elif target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right

    def get_max(self):
        node = self
        if node == None:
            return None

        while node.right != None:
            node = node.right
        return node.value

    def for_each(self, cb):
        # inorder iterative with stack
        node = self
        s = []  # stack
        while node != None or len(s) > 0:
            if node != None:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                cb(node.value)
                node = node.right
