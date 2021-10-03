
def have_opposite_sign(x, y):
    return (x < 0 and y > 0) or (x > 0 and y < 0)


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        # edge cases
        if n < 2:
            return n
        elif n == 2:
            return 2 if nums[0] != nums[1] else 1
        
        # ith element is the length of the longest wiggle sequence that starts at nums[i]
        # answer will be max(dp)
        dp = [1]*(n-1)
        for i in range(n-1):
            lb = i
            ub = i+1
            if nums[lb] != nums[ub]:
                curr_len = 2
            else:
                curr_len = 1
            prev_diff = nums[lb] - nums[ub]
            while ub < n:
                curr_diff = nums[ub-1] - nums[ub]
                if have_opposite_sign(prev_diff, curr_diff):
                    curr_len += 1
                    prev_diff = curr_diff
                ub += 1
            dp[i] = curr_len
            if curr_len >= (n - (lb+1)):
                break
        return max(dp)
