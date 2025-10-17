class Solution:
    def finalString(self, s: str) -> str:
        while "i" in s:
            index = s.index("i")
            first = s[:index][::-1]
            last = s[index+1:]
            s = "".join([first,last])
        return s
print(Solution().finalString(s = "poiinter"))