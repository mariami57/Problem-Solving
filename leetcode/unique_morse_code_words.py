from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dicti = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
                 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
                 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
                 'y': "-.--", 'z': "--.."}

        transformations = set()

        for word in words:
            curr_form = ''
            for char in word:
                curr_form += dicti[char]

            if curr_form not in transformations:
                transformations.add(curr_form)

        return len(transformations)

print(Solution().uniqueMorseRepresentations(["gin","zen","gig","msg"]))
print(Solution().uniqueMorseRepresentations(["a"]))
