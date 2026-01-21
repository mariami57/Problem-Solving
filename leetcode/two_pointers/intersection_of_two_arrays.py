from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = set()

        s1 = 0
        s2 = 0
        e1 = len(nums1)
        e2 = len(nums2)

        while s1 < e1 and s2 < e2:
            if nums1[s1] == nums2[s2]:
                intersection.add(nums1[s1])
                s1 += 1
                s2 += 1

            elif nums1[s1] < nums2[s2]:
                s1 += 1
            else:
                s2 += 1

        result = []
        for x in intersection:
            result.append(x)

        return result

print(Solution().intersection([4,9,5], [9,4,9,8,4]))
