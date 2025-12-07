# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         char_index_s = {}
#         char_index_t = {}
#
#         for i in range(len(s)):
#             if s[i] not in char_index_s:
#                 char_index_s[s[i]] = i
#             if t[i] not in char_index_t:
#                 char_index_t[t[i]] = i
#
#             if char_index_s[s[i]] != char_index_t[t[i]]:
#                 return False
#         return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapped = {}

        for sc, tc in zip(s,t):
            if sc in mapped:
                if mapped[sc] != tc:
                    return False
            elif tc in mapped.values():
                return False

            mapped[sc] = tc

        return True

print(Solution().isIsomorphic(s = "foo", t = "bar"))
print(Solution().isIsomorphic(s = "badc", t = "baba"))
print(Solution().isIsomorphic(s = "egg", t = "add"))

