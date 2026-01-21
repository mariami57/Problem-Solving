from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = set()
        used = [False] * len(digits)

        def backtrack(path):
            if len(path) == 3:
                res.add(path[0] * 100 + path[1] * 10 + path[2])
                return

            for i in range(len(digits)):
                if used[i] == True:
                    continue

                if len(path) == 0 and digits[i] == 0:
                    continue

                if len(path) == 2 and digits[i] % 2 != 0:
                    continue

                used[i] = True
                backtrack(path + [digits[i]])
                used[i] = False
        backtrack([])
        return len(res)

print(Solution().totalNumbers([1,2,3,4]))