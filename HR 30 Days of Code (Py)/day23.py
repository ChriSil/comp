import sys


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
myTree.levelOrder(root)
print('datwaret')
