class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        step = 2 * k
        l = list(s)
        for i in range(0, len(l), step):
            start = i
            end = min(i+k -1, len(l) - 1)
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1
        return ''.join(l)

print(Solution().reverseStr("abcdefg", 2))