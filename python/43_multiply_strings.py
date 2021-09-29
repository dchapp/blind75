
def single_digit_times_single_digit(lhs, rhs):
    return int(lhs) * int(rhs)

def multi_digit_times_single_digit(lhs, rhs):
    product = 0
    exponent = 0
    for digit_idx in range(len(lhs)-1, -1, -1):
        product += 10**exponent * single_digit_times_single_digit(lhs[digit_idx], rhs)
        exponent += 1
    return product

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        exponent = 0
        for digit_idx in range(len(num2)-1, -1, -1):
            ans += 10**exponent * multi_digit_times_single_digit(num1, num2[digit_idx])
            exponent += 1
        return str(ans)	
