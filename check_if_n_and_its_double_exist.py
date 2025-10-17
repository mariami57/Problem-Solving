from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if i >= 0:
                for j in range(0, len(arr)):
                    if arr[i] == 2 * arr[j] and i != j:
                        return True
        return False

print(Solution().checkIfExist([3,1,7,11]))