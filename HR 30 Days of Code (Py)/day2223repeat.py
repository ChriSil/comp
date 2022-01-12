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

    def getHeight(self, root):
        if root is None:
            return -1  # not just condition for empty tree, also final condition for recursion
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
        return answer
        # Write your code here

    def levelOrder2(self, root):
        Q = []  # queue used for going thru
        if (root.data is not None):
            Q.append(root)  # forgot, else Q is still empty
        answer = ""
        while (Q):  # while its not empty
            # answer stacks up with each iteration
            current = Q[0]
            answer = answer + str(current.data) + " "
            if root.left is not None:
                Q.append(current.left)
            if root.right is not None:
                Q.append(current.right)
            Q.pop(0)  # take out first of queue
        return answer


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
ordr = myTree.levelOrder(root)
print(ordr, 'Geordnet nach Leveln')
height = myTree.getHeight(root)
print('Höhe des BinTree:', height)
