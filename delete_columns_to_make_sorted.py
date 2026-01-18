from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        length = len(strs[0])
        rem = 0
        total_str = len(strs)
        j = 0

        while j < length:
            i = 1
            while i < total_str:
                if ord(strs[i][j]) < ord(strs[i-1][j]):
                    rem += 1
                    break
                i+=1
            i = 0
            j += 1

        return rem



print(Solution().minDeletionSize(["zyx","wvu","tsr"]))
print(Solution().minDeletionSize(["cba","daf","ghi"]))
print(Solution().minDeletionSize(["a","b"]))



