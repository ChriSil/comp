# day 11

if __name__ == '__main__':

    arr = []

    for _ in range(6):  # did not know I could do dis _
        arr.append(list(map(int, input().rstrip().split())))

# Task:print max hour glass sum of array:
# # #
  #
# # #

# test array and indices
# print(arr)
# print(arr[3][2])  # Zeile/Spalte. This Prints Zeile4 Spalte3

# test hour glass sum with fixed Index, works.

'''
# static hourglass
# row1 = [sum(arr[row][col+i]) for i in range(0, 2)] # fancy solution not workable yet
row1 = arr[row][col]+arr[row][col+1]+arr[row][col+2]
row2 = arr[row+1][col+1]
row3 = arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
hourg = row1+row2+row3
print(row1, 'plz be 1')
print(row2, 'plz be 4')
print(row3, 'plz be 2')
'''
#row = 0
#col = 0
maxHG = -99
#hourg = 0
for row in range(6):
    for col in range(5):
        if (row+2 < 6) and (col+2 < 6):
            row1 = arr[row][col]+arr[row][col+1]+arr[row][col+2]
            row2 = arr[row+1][col+1]
            row3 = arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
            hourg = row1+row2+row3
            print(hourg, "each HG")
            if hourg > maxHG:
                maxHG = hourg

print(maxHG)
