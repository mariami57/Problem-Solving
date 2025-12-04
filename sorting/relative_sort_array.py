from typing import List


# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         result = []
#
#         for i in range(len(arr2)):
#             for j in range(len(arr1)):
#                 if arr1[j] == arr2[i]:
#                     result.append(arr1[j])
#                     arr1[j] = -1
#
#         arr1.sort()
#         for num in arr1:
#             if num != -1:
#                 result.append(num)
#         return result

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        result = []
        count_dict = {}
        remaining = []

        for num in arr2:
            count_dict[num] = count_dict.get(num, 0)

        for num in arr1:
            if num not in count_dict:
                remaining.append(num)
            else:
                count_dict[num] += 1

        remaining.sort()

        for num in arr2:
            result.extend([num] * count_dict[num])

        result.extend(remaining)

        return result

print(Solution().relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))