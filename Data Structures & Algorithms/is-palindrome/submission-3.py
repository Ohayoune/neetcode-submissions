class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        s = s.lower()
        while start <= end:
            sVal = ord(s[start])
            if not (97 <=sVal<=122 or 48 <=sVal <= 57):
                start+=1
                continue
            eVal = ord(s[end])
            if not (97 <= eVal <= 122 or 48 <= eVal <=57):
                end -= 1
                continue
            
            if eVal != sVal:
                return False
            else:
                start +=1
                end -= 1
        





        return True
        