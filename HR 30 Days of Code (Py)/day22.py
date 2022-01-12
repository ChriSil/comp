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

    def levelOrder(self, root):
        Q = []
        if (root.data is not None):
            Q.append(root)
        answer = ""
        # if the list has any elements in it, it will return true. Basically, while loop will end if list becomes empty.
        while (Q):
            current = Q[0]
            answer = answer + str(current.data) + " "
            if current.left is not None:
                Q.append(current.left)
            if current.right is not None:
                Q.append(current.right)
            Q.pop(0)
        print(answer)

        # Write your code here


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
print('okedere')
