class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_low = 1
        k_high = max(piles) #high
        k= k_high
        while k_low <= k_high:
            k_mid = (k_low+k_high)//2
            if not is_valid(piles, h, k_mid):
                k_low = k_mid + 1
            else:
                k_high = k_mid - 1
                if k_mid < k:
                    k = k_mid
        return k

def is_valid(piles, h: int, k: int) -> bool:
    total_hours_taken = 0
    for value in piles:
        total_hours_taken += (value+k -1)//k

    return total_hours_taken <= h