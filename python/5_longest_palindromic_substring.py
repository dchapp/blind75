
class Solution:
    def longestPalindrome(self, s: str) -> str:
        seeds = []
        head = 0
        tail = 0
        n = len(s)
        while tail < n:
            while tail < n and s[head] == s[tail]:
                tail += 1
            seeds.append([head, tail])
            head = tail
        #print({tuple(indices): s[indices[0]:indices[1]] for indices in seeds})    
        max_len = 0
        candidate = None
        for seed in seeds:
            head, tail = seed
            #print(f"seed: {s[head:tail]}, head = {head}, tail = {tail}")
            curr_len = tail - head
            while head > 0 and tail < n and s[head-1] == s[tail]:
                head -= 1
                tail += 1
                curr_len += 2
            if curr_len > max_len:
                max_len = curr_len
                candidate = s[head:tail]
                #print(f"candidate: {candidate}")
        return candidate
