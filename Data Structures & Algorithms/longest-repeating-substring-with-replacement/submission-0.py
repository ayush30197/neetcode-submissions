class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_count = 0
        start = 0
        max_window_size = 0
        for index, char in enumerate(s):
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1

            if freq_map[char] > max_count:
                max_count = freq_map[char]

            window_size = index - start + 1
            if window_size - max_count > k:
                char_to_remove = s[start]
                freq_map[char_to_remove] -= 1
                start += 1
                window_size = index - start + 1

            if window_size > max_window_size:
                max_window_size = window_size

        return max_window_size