class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        n_bits = len(bits)
        diff = 32 - n_bits
        padded = "".join(['0']*diff) + bits
        val = 0
        exponent = 0
        for i in range(len(padded)):
            current_bit = padded[i]
            val += int(current_bit) * (2**exponent)
            exponent += 1
        return val
