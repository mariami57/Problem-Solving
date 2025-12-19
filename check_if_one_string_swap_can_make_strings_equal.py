class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        i = 0
        j = len(s1) - 1

        while i <= j and s1[i] == s2[i]:
            i += 1

        while j >= 0 and s1[j] == s2[j]:
            j -= 1

        if i < j:
            s1_list = list(s1)
            s1_list[i], s1_list[j] = s1_list[j], s1_list[i]
            s1 = ''.join(s1_list)

        return s1 == s2

print(Solution().areAlmostEqual(s1 = "bank", s2 = "kanb"))
print(Solution().areAlmostEqual(s1 = "attack", s2 = "defend"))
print(Solution().areAlmostEqual(s1 = "kelb", s2 = "kelb"))



