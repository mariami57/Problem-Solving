class Solution:
    def romanToInt(self, s: str) -> int:

        main_romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        int_roman = 0

        for index in range(len(s)):
            current = main_romans[s[index]]
            next = main_romans[s[index + 1]] if index + 1 < len(s) else 0

            if current < next:
                int_roman -= current
            else:
                int_roman += current



        return int_roman

print (Solution().romanToInt("MCMXCIV"))

