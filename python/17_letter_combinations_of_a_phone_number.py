num_to_letters = {
    '2': ['a', 'b', 'c'],    
    '3': ['d', 'e', 'f'],    
    '4': ['g', 'h', 'i'],    
    '5': ['j', 'k', 'l'],    
    '6': ['m', 'n', 'o'],    
    '7': ['p', 'q', 'r', 's'],    
    '8': ['t', 'u', 'v'],    
    '9': ['w', 'x', 'y', 'z'],    
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self.recursive(digits)
    
    
    def recursive(self, digits):
        words = set()
        digit_idx = 0
        def worker(digits, digit_idx, current_word):
            candidates = num_to_letters[digits[digit_idx]]
            for c in candidates:
                if digit_idx == len(digits)-1:
                    words.add(current_word + c)
                else:
                    worker(digits, digit_idx+1, current_word + c)
                    
        worker(digits, 0, "")
        return list(words)
       
