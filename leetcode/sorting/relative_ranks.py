from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(list(set(score)))[::-1]
        result = []
        for s in score:
            if s == sorted_score[0]:
                result.append("Gold Medal")
            elif s == sorted_score[1]:
                result.append("Silver Medal")
            elif s == sorted_score[2]:
                result.append("Bronze Medal")
            else:
                result.append(str(sorted_score.index(s)+1))
        return result

print(Solution().findRelativeRanks([5,4,3,2,1]))
print(Solution().findRelativeRanks([10,3,8,9,4]))