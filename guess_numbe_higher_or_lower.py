PICKED = 2

def guess(num: int) -> int:
    if num > PICKED:
        return -1
    elif num < PICKED:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
       first = 1
       last = n
       mid = 0
       while first <= last:
           mid = (first + last) // 2
           if guess(mid) == 0:
               return mid
           elif guess(mid) == 1:
               first = mid + 1
           else:
               last = mid - 1
       return mid

print(Solution().guessNumber(2))
