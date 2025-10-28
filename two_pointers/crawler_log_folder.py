import re
from typing import List


# class Solution:
#     def minOperations(self, logs: List[str]) -> int:
#         folder_depth = 0
#         pattern = r'[a-z0-9\/]'
#         for i in range(len(logs)):
#             if logs[i] == '../' and folder_depth > 0:
#                 folder_depth -= 1
#             elif logs[i] == './':
#                 continue
#
#             if re.match(pattern, logs[i]):
#                 folder_depth += 1
#
#         return folder_depth

#
# class Solution:
#     def minOperations(self, logs: List[str]) -> int:
#         folder_depth = 0
#
#         for i in range(len(logs)):
#             if logs[i] == '../':
#                 folder_depth = max(0, folder_depth -1)
#             elif logs[i] != './':
#                 folder_depth += 1
#
#         return folder_depth

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for log in logs:
            if log == './' or (log=='../' and ops == 0):
                continue
            elif log=='../' and ops > 0:
                ops -= 1
            else:
                ops += 1
        return ops

print(Solution().minOperations(logs = ["d1/","d2/","../","d21/","./"]))
print(Solution().minOperations(["./","../","./"]))
print(Solution().minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))