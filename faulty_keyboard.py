class Solution:
    def finalString(self, s: str) -> str:
        l = list(s)
        for index in range(len(l)):
            if l[index] == 'i':
                l[:index] = l[:index][::-1]
        while 'i' in l:
            l.remove('i')
        return "".join(l)

print(Solution().finalString(s = "poiinter"))