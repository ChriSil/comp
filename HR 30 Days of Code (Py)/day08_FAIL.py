# Enter your code here. Read input from STDIN. Print output to STDOUT
phonebook = {}
num = int(input().strip())

for i in range(0, num):
    entry = input().split()
    name = entry[0]
    number = int(entry[1])
    phonebook[name] = number


for i in range(0, num):
    name = input()
    if name in phonebook:
        print(name+"="+str(phonebook[name]))
    else:
        print("Not found")


# split line input by space delim
#the_string = raw_input()
#name, age = the_string.split()


# needed some help on this one, but def. learned something.

# currently runs into runtime error. Too slow with 10^5 test cases
