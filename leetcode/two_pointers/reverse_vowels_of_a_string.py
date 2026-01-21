class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left].lower() not in vowels:
                left += 1
            if  s[right].lower() not in vowels:
                right -= 1


        return ''.join(s)


print(Solution().reverseVowels(s = "IceCreAm"))

