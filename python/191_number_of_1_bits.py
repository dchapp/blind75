
def one_liner(n: int) -> int:
    return len(list(filter(lambda b: b == '1', bin(n)[2:])))

def iterative(n: int) -> int:
    count = 0
    for b in bin(n)[2:]:
        if b == '1':
            count += 1
    return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        return iterative(n)
        
