class Solution:
    def myAtoi(self, s: str) -> int:
        maxint = 2**31 - 1
        minint = -2**31
        i, n = 0, len(s)

        while i < n and s[i] == " ":  
            i += 1

        if i == n:
            return 0

        sign = 1
        if i < n and s[i] == "+":     
            i += 1
        elif i < n and s[i] == "-":    
            sign = -1
            i += 1

        rev = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            rev = rev * 10 + digit

            if rev > maxint:           
                return maxint if sign == 1 else minint
            i += 1

        return sign * rev