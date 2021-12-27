# This one took me a long time. Failed iterating over the length of chars and adding evens and odds. Ended up finding the str[start:stop:step] thing and used it.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# if __name__ == '__main__':
# T = # number of test cases
# S = # Strings


#from _typeshed import SupportsRDivMod


T = int(input().strip())
for i in range(0, T):
    S = str(input().strip())
    print(S[::2], S[1::2])  # cheated, stole this [start:stop:step]

    #N = len(S)
'''    #sodd = ""
    #sev = ""
    for j in range(0, N):  # iterate through chars
        s_even = ''
        s_odd = ''
        if j % 2 == 0:
            s_even + (S[j])
        else:
            s_odd + (S[j])
    print(s_even, '/n', s_odd)
   '''

'''
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")

# First we have to take the input of the number of Strings 

NumberOfStrings = int(input())

# for loop from 0 to the length of the String

for i in range(0, NumberOfStrings):
    
    # Taking input from the User 
    
    string = input()
    
    # The below line has two parts 1. string[::2] & 2. string[1::2].
    # General format is [start:stop:step].
    # 1. string[::2] basically means that start from 0 to the end of the String skipping 2 characters hence taking all even strings 
    # 2. string[1::2] same as the above but we start from 1 and not 0 
    
    print(string[::2],string[1::2])

'''
