from typing import List



class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        new_salary = salary[1:-1]
        return sum(new_salary) / len(new_salary)

print(Solution().average([4000,3000,1000,2000]))
print(Solution().average([1000,2000,3000]))