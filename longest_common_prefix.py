from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list(strs[0])
        for index in range(1, len(strs)):
            while prefix and not strs[index].startswith(''.join(prefix)):
                prefix.pop()

        return ''.join(prefix)


print(Solution().longestCommonPrefix(["flower","flow","flight"]))




