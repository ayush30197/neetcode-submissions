class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_string = ""
        for char in s.strip().lower():
            if char.isalnum():
                lower_string += char

        start = 0
        end = len(lower_string)-1

        while True and start < end:
            if lower_string[start] == lower_string[end]:
                start +=1
                end -= 1
                continue
            return False

        return True