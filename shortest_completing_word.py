from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key=lambda x: len(x))
        char_counter = {}
        flag = 0

        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                char_counter[char] = char_counter.get(char, 0) +1

        for w in words:
            for c in char_counter:
                if c in w and char_counter[c] <= w.count(c):
                   flag += 1
            if flag == len(char_counter):
                return w
            else:
                flag = 0


print(Solution().shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
print(Solution().shortestCompletingWord(licensePlate = "Ah71752", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]))
print(Solution().shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"]))