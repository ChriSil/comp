class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        # pass
        res = []
        for i in range(1, n+1):
            # if n % i == 0:
            # res.append(i)
            # else:
            # pass
            res.append(i) if n % i == 0 else ''
        return sum(res)


my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
