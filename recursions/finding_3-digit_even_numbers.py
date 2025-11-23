from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        used = [False] * len(digits)

        def backtrack(path):
            if len(path) == 3:
                num = path[0] * 100 + path[1] * 10 + path[2]
                result.add(num)
                return

            for i in range(len(digits)):
                if used[i]:
                    continue

                if len(path) == 0 and digits[i] == 0:
                    continue

                if len(path) == 2 and digits[i] % 2 != 0:
                    continue

                used[i] = True
                backtrack(path + [digits[i]])
                used[i] = False
        backtrack([])
        return sorted(result)



print(Solution().findEvenNumbers([2,1,3,0]))



