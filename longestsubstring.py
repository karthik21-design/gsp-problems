class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxlength=0
        i=0
        charset=set()

        for j in range(n):
            if s[j] not in charset:
                charset.add(s[j])
                maxlength=max(maxlength,j-i+1)
            else:
                while s[j] in charset:
                    charset.remove(s[i])
                    i=i+1
                charset.add(s[j])
        return maxlength