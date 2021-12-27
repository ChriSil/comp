import sys


class Solution1:  # did not work, none are palindromes
    def __init__(self):
        self.stack = []  # Stack implemented as a list
        self.queue = []  # Queue implemented as a list

    def pushCharacter(self, ch):  # pushes character on Stack, void
        self.stack.append(ch)

    def enqueueCharacter(self, ch):  # enqueues character in queue instance variable
        self.queue.append(ch)

    def popCharacter(self):  # pops off and returns  char on top of stack
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def dequeueCharacter(self):  # dequeues, returns char back to queue
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    # Write your code here


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def popCharacter(self):
        return self.stack.pop()

    def pushCharacter(self, char):
        self.stack.append(char)

    def dequeueCharacter(self):
        char = self.queue[0]
        self.queue = self.queue[1:]
        return char

    def enqueueCharacter(self, char):
        self.queue.append(char)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
