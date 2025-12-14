from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0

        for i in range(len(timeSeries)-1):
            result += min(timeSeries[i+1]-timeSeries[i], duration)

        result += duration
        return result

print(Solution().findPoisonedDuration(timeSeries = [1,4], duration = 2))
print(Solution().findPoisonedDuration(timeSeries = [1,2], duration = 2))
print(Solution().findPoisonedDuration(timeSeries = [1,2,3,4,5], duration = 5))

