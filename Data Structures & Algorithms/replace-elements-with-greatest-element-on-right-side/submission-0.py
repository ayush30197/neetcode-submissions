class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        for _ in arr:
            j = i+1
            max_element_to_right = -1
            for next_index in range(j, len(arr)):
                if arr[next_index] > max_element_to_right:
                    max_element_to_right = arr[next_index]

            arr[i] = max_element_to_right
            i += 1

        return arr