from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = []
        curr_line = 0
        lines = 0

        for char in s:
            idx = (ord(char) - 97)
            if curr_line + widths[idx] <= 100:
                curr_line += widths[idx]
            else:
                lines += 1
                curr_line = widths[idx]
        lines += 1

        result.append(lines)
        result.append(curr_line)

        return result


print(Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                                s = "bbbcccdddaaa"))
print(Solution().numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                               s = "abcdefghijklmnopqrstuvwxyz"))



