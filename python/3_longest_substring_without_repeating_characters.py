class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len = 1
        head = 0
        tail = 0
        char_set = set()
        s_len = len(s)
        while tail < s_len:
            if s[tail] not in char_set:
                char_set.add(s[tail])
                tail += 1
                new_len = tail - head
                if new_len > max_len:
                    max_len = new_len
            else:
                char_set.remove(s[head])
                head += 1
        return max_len
