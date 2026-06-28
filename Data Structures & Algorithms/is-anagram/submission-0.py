class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_hash_table = [0]*26
        for i in range(len(s)):
            my_hash_table[ord(s[i])-ord('a')] += 1
            my_hash_table[ord(t[i]) - ord('a')] -= 1

        for val in my_hash_table:
            if val!=0:
                return False
        return True