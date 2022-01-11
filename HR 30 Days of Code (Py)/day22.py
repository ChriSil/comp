class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    # Idea: recursive function for going thru tree, v1
    # def baseOp(self, root):
    #    if root.left or root.right is not None:
    #        height = height + 1
    #        baseOp(root.left)
    #        baseOp(root.right)
    #    else:
    #        return
    # def getHeight(self, root):

    #    if root is  not None:
    #        height = -
    #    if root.left or root.right is not None:
    #        height += 1
    #        self.getHeight(root.left)
    #        self.getHeight(root.right)
    #    return height
        # Write your code here
    # more elegant solution found. but recursion was good!
    def getHeight(self, root):
        if root is None:
            return -1
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
print('okedere')
