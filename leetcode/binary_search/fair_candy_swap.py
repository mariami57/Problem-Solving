from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        diff = (alice_sum - bob_sum) // 2
        bob_set = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in bob_set:
                return [a, b]

print(Solution().fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))



