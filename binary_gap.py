class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        count_ones = bin_n.count('1')

        if count_ones <= 1:
            return 0

        max_dist = 0
        i = 0

        while i < len(bin_n)-1:
            dist = 0
            if bin_n[i] == '1':
                count_ones -= 1
                i += 1
                dist += 1
                while bin_n[i] == '0' and i < len(bin_n)-1 and count_ones > 0:
                    dist += 1
                    i+= 1

            else:
                i += 1
            max_dist = max(max_dist, dist)

        return max_dist

print(Solution().binaryGap(12))
print(Solution().binaryGap(13))
print(Solution().binaryGap(7))
print(Solution().binaryGap(22))
print(Solution().binaryGap(8))
print(Solution().binaryGap(5))

