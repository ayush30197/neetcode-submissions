class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        len_of_smallest_word = len(strs[0])
        smallest_word = strs[0]

        for word in strs:
            if len(word) < len_of_smallest_word:
                len_of_smallest_word = len(word)
                smallest_word = word

        i = 0
        while i < len_of_smallest_word:
            for word in strs:
                if word[i] != smallest_word[i]:
                    return smallest_word[:i]
            i += 1

        return smallest_word