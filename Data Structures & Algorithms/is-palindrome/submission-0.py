class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join([t for t in s if t.isalnum()]).lower()
        return text == text[-1::-1]
        