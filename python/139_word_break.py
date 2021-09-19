class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Preprocess
        query_alphabet = set(s)
        dict_alphabet = set(''.join(x for x in wordDict))
        for x in query_alphabet:
            if x not in dict_alphabet:
                return False
        
        word_set = set(wordDict) 
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                # dp[j] == True --> prefix is in word_set
                # s[j:i] is suffix starting from i and looking j ahead
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
