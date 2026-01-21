class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0].lower() not in vowels:
                sentence[i] = sentence[i][1:] + sentence[i][0]
            sentence[i] += 'ma' + ('a' * (i+1))
        return ' '.join(sentence)

print(Solution().toGoatLatin("I speak Goat Latin"))
print(Solution().toGoatLatin("The quick brown fox jumped over the lazy dog"))