class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercaseStr=""
        for char in s:
            if char.isdigit() or char.isalpha():
                lowercaseStr+=char.lower()
        return lowercaseStr==lowercaseStr[::-1]
            

        