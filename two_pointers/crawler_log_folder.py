import re
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0
        pattern = r'[a-z0-9\/]'
        for i in range(len(logs)):
            if logs[i] == '../' and folder_depth > 0:
                folder_depth -= 1
            elif logs[i] == './':
                continue

            if re.match(pattern, logs[i]):
                folder_depth += 1

        return folder_depth


print(Solution().minOperations(["./","../","./"]))