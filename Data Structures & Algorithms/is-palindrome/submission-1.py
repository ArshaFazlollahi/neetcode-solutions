class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        sArray = list(string)
        left = 0
        right = len(sArray) - 1
        sAlphanumeric = "0123456789abcdefghijklmnopqrstuvwxyz"
        alphanumeric = list(sAlphanumeric)
        while left<right:
            if sArray[left] not in alphanumeric:
                left = left + 1
                continue
            if sArray[right] not in alphanumeric:
                right = right - 1
                continue
            if sArray[left] != sArray[right]:
                return False
            left = left + 1
            right = right - 1
        return True