from lab0_utilities import *


class BalancingTree:
    def __init__(self, root_node):
        self.root = root_node

    # Function used in balanced_insert and in grading rotations directly
    def insert(self, node, curr=None):
        curr = curr if curr else self.root
        # Recurse to right spot
        if node._val < curr._val:
            if curr.left is not None:
                self.insert(node, curr.left)
            else:
                node.parent = curr
                curr.left = node
        elif node._val > curr._val:
            if curr.right is not None:
                self.insert(node, curr.right)
            else:
                node.parent = curr
                curr.right = node
        else:
            curr.val.append(node.val[0])
            return 1
        return 0

    def balanced_insert(self, node, curr=None):
        curr = curr if curr else self.root
        z = self.insert(node, curr)
        if (z != 1):
            self.balance_tree(node)
        return

    # Check balance manually with heights for grading purposes
    # Commented code for checking balance with bf's
    def find_height(self, root):
        if not root:
            return 0
        return 1 + max(self.find_height(root.left), self.find_height(root.right))

    def is_balanced(self):
        root = self.root

        def isBalancedHelper(root):
            if root is None:
                return True
            h1 = self.find_height(root.left)
            h2 = self.find_height(root.right)
            if abs(h1 - h2) < 2 and isBalancedHelper(root.left) and isBalancedHelper(root.right):
                return True
            return False

        return isBalancedHelper(root)

    # NOTE - Balancing done with heights and not bf with a default height of 1
    # avl_trees_tester.py exercises gives the balance implementation using bf's
    # Needs to be modified if using default height of 0
    # maximum abs(bf) = 2 (usually never happens), modify for 1

    def balance_tree(self, node):
        # Bubbles up from inserted node -> check avl_trees_tester for implementation that starts from root
        while node is not None:
            self.update_height(node)
            if self.height(node.left) >= 2 + self.height(node.right):
                if self.height(node.left.left) >= self.height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif self.height(node.right) >= 2 + self.height(node.left):
                if self.height(node.right.right) >= self.height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    # Change left and right rotate to avl_trees_tester for for default height 0 and balancing with bf
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        self.update_height(x)
        self.update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        self.update_height(x)
        self.update_height(y)

    ### Extra helper functions from here

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def height(self, node):
        return node.height if node else -1

    def inOrder(self, root):
        result = []
        if root:
            result += self.inOrder(root.left)
            result.append(root.val)
            result += self.inOrder(root.right)
        return result

    count = 0

    def preorder_count(self, node):
        if node is None:
            return
        self.count += 1
        self.preorder_count(node.left)
        self.preorder_count(node.right)
        return self.count

    def preOrder(self, root):
        result = []
        if root:
            result.append(root._val)
            result += self.preOrder(root.left)
            result += self.preOrder(root.right)
        return result

    def maximum(self, root: Node):
        while root.right:
            root = root.right
        return root

    def minimum(self, root: Node):
        # Try implementing (similar to maximum)
        while root.left:
            root = root.left
        return root

    def predecessor(self, n: Node):
        if n.left:
            return self.maximum(n.left)
        while n and n == n.parent.left:
            n = n.parent
        return n.parent

    def successor(self, n: Node):
        # Try implementing (similar to predecessor)
        if n.right:
            return self.minimum(n.right)
        while n and n == n.parent.right:
            n = n.parent
        return n.parent

        def search(self, key):
            root = self.root
            while root and not root._val == key:
                if key < root._val:
                    root = root.left
                else:
                    root = root.right
            return root

        def delete(self, n):
            
            def replace(root, n1, n2):
                if not n1.parent:
                    root = n2
                elif n1 == n1.parent.left:
                    n1.parent.left = n2
                else:
                    n1.parent.right = n2
                if n2:
                    n2.parent = n1.parent
                return root

            def minimum_node(n):
                while n.left:
                    n = n.left
                return n

            if not n.left:
                self.root = replace(self.root, n, n.right)
            elif not n.right:
                self.root = replace(self.root, n, n.left)
            else:
                m = minimum_node(n.right)
                if m.parent is not n:
                    self.root = replace(self.root, m, m.right)
                    m.right, m.right.parent = n.right, m
                self.root = replace(self.root, n, m)
                m.left = n.left
                m.left.parent = m

        def search_and_delete(self, key):
            node = self.search(key)
            if node:
                self.delete(node)
            else: return None
    '''
    if __name__ == '__main__':
        tree = BalancingTree(Node(Word('hips','body part')))
        tree.balanced_insert(Node(Word('jello', 'food')))
        tree.balanced_insert(Node(Word('volleyball', 'sport')))
        tree.balanced_insert(Node(Word('dog', 'a friendly animal')))
        sm = tree.inOrder(tree.root)
        for i in sm:
            print(i[0])
        tree.search_and_delete('jello')
        print('should be deleted')
        sm = tree.inOrder(tree.root)
        for i in sm:
            print(i[0])
        print('should be balanced')
        tree.balance_tree(tree.root)
        sm = tree.inOrder(tree.root)
        for i in sm:
            print(i[0])
        tree.search_and_delete('hips')
        print('should be deleted')
        sm = tree.inOrder(tree.root)
        for i in sm:
            print(i[0])
        print('should be balanced')
        tree.balance_tree(tree.root)
        sm = tree.inOrder(tree.root)
        for i in sm:
            print(i[0])
    '''
