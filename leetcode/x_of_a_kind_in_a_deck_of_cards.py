from collections import Counter
from math import gcd
from typing import List

from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False

        counts = Counter(deck)
        vals = list(counts.values())
        gd = reduce(gcd, vals)
        return True if gd > 1 else False

print(Solution().hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1]))
print(Solution().hasGroupsSizeX(deck = [1]))
print(Solution().hasGroupsSizeX(deck = [1,1,1,2,2,2,3,3]))

