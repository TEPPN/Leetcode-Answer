#My Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        for i in range (n):
            for j in range (i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j
                j+=1
            i+=1

#More Efficient
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         num_map = {}  
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:                    
#               return [num_map[complement], i]
#             num_map[num] = i
#             return []