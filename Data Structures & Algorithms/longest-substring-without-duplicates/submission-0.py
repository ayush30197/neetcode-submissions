class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_hash_map = {}
        max_len = 0
        start = 0

        for index in range(len(s)):
            char = s[index]

            if char in sub_hash_map:
                prev_index = sub_hash_map[char]
                if prev_index>= start:
                    start = prev_index + 1

            sub_hash_map[char] = index
            len_of_substring = (index - start) + 1
            if len_of_substring > max_len:
                max_len = len_of_substring

        return max_len