from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        op = 0
        bits = bits[::-1]
        while bits:
            op = bits.pop()
            if op:
                bits.pop()
        return not op

print(Solution().isOneBitCharacter([1,0,0]))
print(Solution().isOneBitCharacter([1,1,1,0]))


