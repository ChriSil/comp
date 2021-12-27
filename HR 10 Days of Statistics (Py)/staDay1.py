# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as sta

# N = 10
# Narr = (64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060)
if __name__ == '__main__':
    N = int(input())
    Narr = list(map(int, input().split()))
    print(sta.mean(Narr))    # Mean 1 decimal place
    print(sta.median(Narr))
    # Median, 1 decimal place
    print(min(sta.multimode(Narr)))    # Mode,if more than one, print smallest
