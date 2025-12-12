class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        some_s = s.replace('-', '').upper()

        mod = len(some_s) % k
        parts = []

        if mod > 0:
            parts.append(some_s[:mod])

        for i in range(mod, len(some_s), k):
            parts.append(some_s[i:i+k])

        return '-'.join(parts)

print(Solution().licenseKeyFormatting(s = "2-5g-3-J", k = 2))
print(Solution().licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
