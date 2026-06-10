class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 0:
            return s
        
        maxlen = 1
        n = len(s)
        maxstring =s [0]
        for i in range(n-1):
            for j in range(i+1,n):
                while j-i+1 > maxlen and s[i:j+1]==s[i:j+1][::-1]:
                    maxstring=s[i:j+1]
                    maxlen=j-i+1
        return maxstring
                    

