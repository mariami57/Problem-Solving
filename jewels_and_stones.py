class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for char in jewels:
            count += stones.count(char)
        return count

print(Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(Solution().numJewelsInStones(jewels = "z", stones = "ZZ"))
