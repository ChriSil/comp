# Write your code here
class Calculator:
    # def __init__(self):

    def power(self, bse, pwr):
        if (bse < 0 or pwr < 0):
            raise Exception("n and p should be non-negative")
        else:
            res = pow(bse, pwr)
            return(res)


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
